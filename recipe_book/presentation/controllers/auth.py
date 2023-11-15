from uuid import uuid4

from fastapi import APIRouter, Depends, Header, Cookie
from fastapi.security import OAuth2PasswordRequestForm
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_422_UNPROCESSABLE_ENTITY

from application_core.users.interfaces.access_token_creator import ITokenCreator
from application_core.users.interfaces.password_hasher import IPasswordHasher
from application_core.users.interfaces.token import IAccessTokenData
from application_core.users.interfaces.user_entity import IUserEntity
from application_core.users.interfaces.users_service import IUsersService

from dependencies import oauth2_scheme, create_token_creator, create_users_service, create_password_hasher

from settings import settings

from ..beans.token import AccessTokenData

router = APIRouter(prefix="/auth", tags=["auth"])

TOKEN_TYPE = "bearer"


async def get_login_from_form(form_data: OAuth2PasswordRequestForm = Depends()) -> str | None:
    return form_data.username


async def get_password_from_form(form_data: OAuth2PasswordRequestForm = Depends()) -> str | None:
    return form_data.password


async def get_access_token_data(access_token: str | None = Depends(oauth2_scheme)) -> IAccessTokenData | None:
    return AccessTokenData(access_token=access_token, token_type=TOKEN_TYPE) if access_token else None


async def get_login_from_access_token(
    access_token: str | None = Depends(oauth2_scheme),
    token_creator: ITokenCreator = Depends(create_token_creator),
) -> str | None:
    if not access_token:
        return None

    try:
        payload = await token_creator.read(access_token)
        login: str = payload.get("sub")
    except Exception as error:
        # todo: check custom error
        print(error)
        return None

    return login


async def get_login_from_refresh_token(
    refresh_token: str | None = Cookie(default=None, alias=settings.refresh_token_cookie_key),
    token_creator: ITokenCreator = Depends(create_token_creator),
) -> str | None:
    if not refresh_token:
        return None

    try:
        payload = await token_creator.read(refresh_token)
        login: str = payload.get("sub")
    except Exception as error:
        # todo: check custom error
        print(error)
        return None

    return login


async def get_login_from_csrf_token(
    token_creator: ITokenCreator = Depends(create_token_creator),
    csrf_token: str | None = Header(default=None, alias=settings.csrf_token_header_key),
) -> str | None:
    if not csrf_token:
        return None

    try:
        payload = await token_creator.read(csrf_token)
        login: str = payload.get("sub")
    except Exception as error:
        # todo: check custom error
        print(error)
        return None

    return login


async def get_current_user(
    login: str | None = Depends(get_login_from_access_token),
    user_service: IUsersService = Depends(create_users_service),
) -> IUserEntity | None:
    if not login:
        return None

    user = await user_service.get_user_by_login(login)

    if user and not user.is_removed:
        return user


async def get_current_active_user(current_user: IUserEntity | None = Depends(get_current_user)) -> IUserEntity | None:
    if current_user and current_user.is_active:
        return current_user


async def check_user_authorization(current_user: IUserEntity | None = Depends(get_current_active_user)) -> None:
    if not current_user:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Not authenticated")


async def check_csrf_token(request: Request, login: str | None = Depends(get_login_from_csrf_token)) -> None:
    request_method = request.method.lower()
    if request_method in ("post", "put", "patch", "delete") and not login:
        raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="CSRF token has expired")


async def create_csrf_token(
    request: Request,
    response: Response,
    authenticated_login: str | None = Depends(get_login_from_access_token),
    csrf_login: str | None = Depends(get_login_from_csrf_token),
    token_creator: ITokenCreator = Depends(create_token_creator),
) -> None:
    request_method = request.method.lower()
    login = authenticated_login or csrf_login or str(uuid4())

    if login and request_method in ("get", "head", "options"):
        new_csrf_token = await token_creator.create_csrf_token(data={"sub": login})
        response.headers[settings.csrf_token_header_key] = new_csrf_token


async def create_access_token_data(login: str, token_creator: ITokenCreator, response: Response) -> IAccessTokenData:
    access_token = await token_creator.create_access_token(data={"sub": login})
    refresh_token = await token_creator.create_refresh_token(data={"sub": login})
    response.set_cookie(
        key=settings.refresh_token_cookie_key, value=refresh_token, samesite="strict", httponly=True, secure=True
    )
    return AccessTokenData(access_token=access_token, token_type=TOKEN_TYPE)


async def create_access_token(
    response: Response,
    login: str = Depends(get_login_from_form),
    password: str = Depends(get_password_from_form),
    user_service: IUsersService = Depends(create_users_service),
    passwordHasher: IPasswordHasher = Depends(create_password_hasher),
    token_creator: ITokenCreator = Depends(create_token_creator),
) -> IAccessTokenData:
    user = await user_service.get_user_by_login(login)

    if (
        not user
        or user.is_removed
        or not user.is_active
        or not await passwordHasher.verify(user.password_hash, password)
    ):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return await create_access_token_data(login, token_creator, response)


async def refresh_access_token(
    response: Response,
    current_active_user: IUserEntity | None = Depends(get_current_active_user),
    login: str = Depends(get_login_from_refresh_token),
    user_service: IUsersService = Depends(create_users_service),
    token_creator: ITokenCreator = Depends(create_token_creator),
) -> IAccessTokenData:
    if current_active_user:
        raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Access token has not expired")

    if not login:
        raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Refresh token is required")

    user = await user_service.get_user_by_login(login)

    if not user or user.is_removed or not user.is_active:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Not authenticated")

    return await create_access_token_data(login, token_creator, response)


@router.get("/token")
async def get_access_token(access_token_data: IAccessTokenData | None = Depends(get_access_token_data)) -> None:
    return access_token_data


@router.post("/token", response_model=AccessTokenData, dependencies=[Depends(check_csrf_token)])
async def issue_access_token(access_token_data: IAccessTokenData = Depends(create_access_token)) -> IAccessTokenData:
    return access_token_data


@router.post("/refresh", response_model=AccessTokenData)
async def refresh_access_token(access_token_data: IAccessTokenData = Depends(refresh_access_token)) -> IAccessTokenData:
    return access_token_data


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key=settings.refresh_token_cookie_key, samesite="strict", httponly=True, secure=True)
