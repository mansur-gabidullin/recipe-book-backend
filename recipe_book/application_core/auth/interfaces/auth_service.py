from typing import Protocol, runtime_checkable

from ...users.interfaces.user_entity import IUserEntity

from .access_token import IAccessToken
from .csrf_token import ICsrfToken
from .refresh_token import IRefreshToken


@runtime_checkable
class IAuthService(Protocol):
    async def verify_hash(self, hash_: str, password: str) -> bool:
        ...

    async def create_csrf_token(self, data: dict) -> ICsrfToken:
        ...

    async def create_access_token(self, data: dict) -> IAccessToken:
        ...

    async def create_refresh_token(self, data: dict) -> IRefreshToken:
        ...

    async def get_current_user(self, access_token: IAccessToken | None) -> IUserEntity | None:
        ...

    async def get_current_active_user(self, access_token: IAccessToken | None) -> IUserEntity | None:
        ...

    async def get_login_from_csrf_token(self, csrf_token: ICsrfToken) -> str | None:
        ...

    async def get_login_from_access_token(self, access_token: IAccessToken) -> str | None:
        ...

    async def get_login_from_refresh_token(self, refresh_token: IRefreshToken) -> str | None:
        ...
