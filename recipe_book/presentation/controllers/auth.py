from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_422_UNPROCESSABLE_ENTITY

from application_core.users.interfaces.access_token_creator import ITokenCreator
from application_core.users.interfaces.password_hasher import IPasswordHasher
from application_core.users.interfaces.token import IAccessTokenData
from application_core.users.interfaces.user import IUser
from application_core.users.interfaces.user_result import IUserResult
from application_core.users.interfaces.users_service import IUsersService

from dependencies import oauth2_scheme, create_token_creator, create_users_service, create_password_hasher

from settings import settings

from ..beans.token import AccessTokenData
from ..beans.users_query import UsersQuery

router = APIRouter(prefix="/auth", tags=["auth"])


async def get_login_from_form(form_data: OAuth2PasswordRequestForm = Depends()) -> str | None:
    return form_data.username


async def get_password_from_form(form_data: OAuth2PasswordRequestForm = Depends()) -> str | None:
    return form_data.password


async def get_login_from_access_token(
    access_token: str | None = Depends(oauth2_scheme),
    token_creator: ITokenCreator = Depends(create_token_creator),
) -> str | None:
    if not access_token:
        return None

    try:
        payload = await token_creator.read(access_token)
        login: str = payload.get("sub")
    except Exception:
        # todo: check custom error
        return None

    return login


async def get_login_from_refresh_token(
    request: Request,
    token_creator: ITokenCreator = Depends(create_token_creator),
) -> str | None:
    refresh_token = request.cookies.get(settings.refresh_token_cookie_key)

    if not refresh_token:
        return None

    try:
        payload = await token_creator.read(refresh_token)
        login: str = payload.get("sub")
    except Exception:
        # todo: check custom error
        return None

    return login


async def get_current_user(
    login: str | None = Depends(get_login_from_access_token),
    user_service: IUsersService = Depends(create_users_service),
) -> IUser | None:
    if not login:
        return None

    user: IUser | None
    [user] = await user_service.get_users_list(UsersQuery(login=login, limit=1))

    if user and not user.is_removed:
        return user


async def get_current_active_user(current_user: IUser | None = Depends(get_current_user)) -> IUser | None:
    if current_user and current_user.is_active:
        return current_user


def check_user_authorization(current_user: IUser | None = Depends(get_current_active_user)) -> None:
    if not current_user:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def create_access_token(
    response: Response,
    login: str = Depends(get_login_from_form),
    password: str = Depends(get_password_from_form),
    user_service: IUsersService = Depends(create_users_service),
    passwordHasher: IPasswordHasher = Depends(create_password_hasher),
    token_creator: ITokenCreator = Depends(create_token_creator),
) -> IAccessTokenData:
    user: IUserResult | None
    [user] = await user_service.get_users_list(UsersQuery(login=login, limit=1))

    if (
        not user
        or user.is_removed
        or not user.is_active
        or not await passwordHasher.verify(user.password_hash, password)
    ):
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Not authenticated")

    access_token = await token_creator.create_access_token(data={"sub": login})
    refresh_token = await token_creator.create_refresh_token(data={"sub": login})
    response.set_cookie(key=settings.refresh_token_cookie_key, value=refresh_token, httponly=True)

    return AccessTokenData(access_token=access_token, token_type="bearer")


async def refresh_access_token(
    response: Response,
    current_active_user: IUser | None = Depends(get_current_active_user),
    login: str = Depends(get_login_from_refresh_token),
    user_service: IUsersService = Depends(create_users_service),
    token_creator: ITokenCreator = Depends(create_token_creator),
) -> IAccessTokenData:
    if current_active_user:
        raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Access token has not expired")

    if not login:
        raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Refresh token is required")

    user: IUserResult | None
    [user] = await user_service.get_users_list(UsersQuery(login=login, limit=1))

    if not user or user.is_removed or not user.is_active:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Not authenticated")

    access_token = await token_creator.create_access_token(data={"sub": login})
    refresh_token = await token_creator.create_refresh_token(data={"sub": login})
    response.set_cookie(key=settings.refresh_token_cookie_key, value=refresh_token, httponly=True)

    return AccessTokenData(access_token=access_token, token_type="bearer")


@router.post("/token", response_model=AccessTokenData)
async def generate_access_token(access_token_data: IAccessTokenData = Depends(create_access_token)) -> IAccessTokenData:
    return access_token_data


@router.post("/refresh", response_model=AccessTokenData)
async def refresh_access_token(access_token_data: IAccessTokenData = Depends(refresh_access_token)) -> IAccessTokenData:
    return access_token_data


@router.post("/logout")
async def remove_refresh_token(response: Response):
    response.delete_cookie(key=settings.refresh_token_cookie_key, httponly=True)
