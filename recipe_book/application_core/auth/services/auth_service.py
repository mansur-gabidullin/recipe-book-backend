from shared_kernal.interfaces.access_token_creator import ITokenCreator
from shared_kernal.interfaces.password_hasher import IPasswordHasher

from ...users.interfaces.user_entity import IUserEntity
from ...users.interfaces.users_service import IUsersService

from ..interfaces.access_token import IAccessToken
from ..interfaces.csrf_token import ICsrfToken
from ..interfaces.refresh_token import IRefreshToken

from ..interfaces.auth_service import IAuthService


class AuthService(IAuthService):
    def __init__(self, token_creator: ITokenCreator, user_service: IUsersService, password_hasher: IPasswordHasher):
        self._token_creator = token_creator
        self._user_service = user_service
        self._password_hasher = password_hasher

    async def verify_hash(self, hash_, password) -> bool:
        return await self._password_hasher.verify(hash_, password)

    async def create_csrf_token(self, data) -> ICsrfToken:
        return ICsrfToken(await self._token_creator.create_csrf_token(data))

    async def create_access_token(self, data) -> IAccessToken:
        return IAccessToken(await self._token_creator.create_access_token(data))

    async def create_refresh_token(self, data) -> IRefreshToken:
        return IRefreshToken(await self._token_creator.create_refresh_token(data))

    async def get_login_from_access_token(self, access_token) -> str | None:
        try:
            payload = await self._token_creator.read(access_token)
            login: str = payload.get("sub")
        except Exception as error:
            # todo: check custom error
            print(error)
            return None

        return login

    async def get_login_from_refresh_token(self, refresh_token) -> str | None:
        if not refresh_token:
            return None

        try:
            payload = await self._token_creator.read(refresh_token)
            login: str = payload.get("sub")
        except Exception as error:
            # todo: check custom error
            print(error)
            return None

        return login

    async def get_login_from_csrf_token(self, csrf_token) -> str | None:
        try:
            payload = await self._token_creator.read(csrf_token)
            login: str = payload.get("sub")
        except Exception as error:
            # todo: check custom error
            print(error)
            return None

        return login

    async def get_current_user(self, access_token) -> IUserEntity | None:
        if not access_token:
            return None

        login = await self.get_login_from_access_token(access_token)

        if not login:
            return None

        user = await self._user_service.get_user_by_login(login)

        if user and not user.is_removed:
            return user

    async def get_current_active_user(self, access_token) -> IUserEntity | None:
        current_user = await self.get_current_user(access_token)

        if current_user and current_user.is_active:
            return current_user
