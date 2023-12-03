from uuid import uuid4

from fastapi import APIRouter, Depends, Header, Cookie
from fastapi.security import OAuth2PasswordRequestForm
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_422_UNPROCESSABLE_ENTITY

from constants import ACCESS_TOKEN_TYPE
from settings import settings

from dependencies import (
    create_users_service,
    create_auth_service,
    oauth2_scheme,
)

from application_core.auth.interfaces.access_token import IAccessToken
from application_core.auth.interfaces.csrf_token import ICsrfToken
from application_core.auth.interfaces.refresh_token import IRefreshToken
from application_core.auth.interfaces.auth_service import IAuthService
from application_core.users.interfaces.users_service import IUsersService

from ..interfaces.auth.access_token_response_model import IAccessTokenResponseModel
from ..beans.auth.access_token_response_model import AccessTokenResponseModel

router = APIRouter(prefix="/auth", tags=["auth"])


def raise_forbidden_error():
    raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Not authenticated")


def raise_unprocessable_entity_error(detail: str):
    raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)


def raise_unauthorized_error(detail: str):
    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail=detail, headers={"WWW-Authenticate": "Bearer"})


async def get_access_token(access_token: str | None = Depends(oauth2_scheme)) -> IAccessToken | None:
    return IAccessToken(access_token) if access_token else None


async def get_csrf_token(
    csrf_token: str | None = Header(default=None, alias=settings.csrf_token_header_key)
) -> ICsrfToken | None:
    return ICsrfToken(csrf_token) if csrf_token else None


async def get_refresh_token(
    refresh_token: str | None = Cookie(default=None, alias=settings.refresh_token_cookie_key)
) -> IRefreshToken | None:
    return IRefreshToken(refresh_token) if refresh_token else None


async def check_access_token(
    auth_service: IAuthService = Depends(create_auth_service),
    access_token: IAccessToken | None = Depends(get_access_token),
) -> None:
    if not access_token:
        raise_forbidden_error()

    current_user = await auth_service.get_current_active_user(access_token)

    if not current_user:
        raise_forbidden_error()


async def check_csrf_token(
    request: Request,
    csrf_token: ICsrfToken | None = Depends(get_csrf_token),
    auth_service: IAuthService = Depends(create_auth_service),
) -> None:
    request_method = request.method.lower()

    if request_method not in ("post", "put", "patch", "delete"):
        return None

    csrf_token_expired_message = "CSRF token has expired"

    if not csrf_token:
        raise_unprocessable_entity_error(csrf_token_expired_message)

    login = await auth_service.get_login_from_csrf_token(csrf_token)

    if not login:
        raise_unprocessable_entity_error(csrf_token_expired_message)


async def issue_csrf_token(
    request: Request,
    response: Response,
    auth_service: IAuthService = Depends(create_auth_service),
    access_token: IAccessToken | None = Depends(get_access_token),
    csrf_token: ICsrfToken | None = Depends(get_csrf_token),
) -> None:
    request_method = request.method.lower()

    if request_method not in ("get", "head", "options"):
        return None

    login = await auth_service.get_login_from_access_token(access_token)

    if not login:
        login = await auth_service.get_login_from_csrf_token(csrf_token)

    if not login:
        # for unauthorized user
        login = str(uuid4())

    new_csrf_token = await auth_service.create_csrf_token({"sub": login})
    response.headers[settings.csrf_token_header_key] = new_csrf_token


def set_refresh_token_cookie(refresh_token: str, response: Response):
    response.set_cookie(
        key=settings.refresh_token_cookie_key, value=refresh_token, samesite="strict", httponly=True, secure=True
    )


@router.get("/token", response_model=AccessTokenResponseModel | None)
async def get_access_token(
    access_token: IAccessToken | None = Depends(get_access_token),
) -> IAccessTokenResponseModel | None:
    return AccessTokenResponseModel(access_token=access_token, token_type=ACCESS_TOKEN_TYPE) if access_token else None


@router.post("/token", response_model=AccessTokenResponseModel, dependencies=[Depends(check_csrf_token)])
async def issue_access_token(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_service: IUsersService = Depends(create_users_service),
    auth_service: IAuthService = Depends(create_auth_service),
) -> IAccessTokenResponseModel:
    login = form_data.username
    password = form_data.password
    user = await user_service.get_user_by_login(login)

    if (
        not user
        or user.is_removed
        or not user.is_active
        or not await auth_service.verify_hash(user.password_hash, password)
    ):
        raise_unauthorized_error("Could not validate credentials")

    refresh_token = await auth_service.create_refresh_token({"sub": login})

    set_refresh_token_cookie(refresh_token, response)

    access_token = await auth_service.create_access_token({"sub": login})

    return AccessTokenResponseModel(access_token=access_token, token_type=ACCESS_TOKEN_TYPE)


@router.post("/refresh", response_model=AccessTokenResponseModel)
async def refresh_access_token(
    response: Response,
    access_token: IAccessToken = Depends(get_access_token),
    refresh_token: IRefreshToken = Depends(get_refresh_token),
    user_service: IUsersService = Depends(create_users_service),
    auth_service: IAuthService = Depends(create_auth_service),
) -> IAccessTokenResponseModel:
    current_active_user = await auth_service.get_current_active_user(access_token)

    if current_active_user:
        raise_unprocessable_entity_error("Access token has not expired")

    login = await auth_service.get_login_from_refresh_token(refresh_token)

    if not login:
        raise_unprocessable_entity_error("Refresh token is required")

    user = await user_service.get_user_by_login(login)

    if not user or user.is_removed or not user.is_active:
        raise_forbidden_error()

    refresh_token = await auth_service.create_refresh_token({"sub": login})

    set_refresh_token_cookie(refresh_token, response)

    access_token = await auth_service.create_access_token({"sub": login})

    return AccessTokenResponseModel(access_token=access_token, token_type=ACCESS_TOKEN_TYPE)


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key=settings.refresh_token_cookie_key, samesite="strict", httponly=True, secure=True)
