from uuid import UUID

from ..interfaces.add_user_command import IAddUserCommand
from ..interfaces.password_hasher import IPasswordHasher
from ..interfaces.remove_user_command import IRemoveUserCommand
from ..interfaces.user import IUser
from ..interfaces.users_query import IUsersQuery
from ..interfaces.users_repository import IUsersRepository
from ..interfaces.users_service import IUsersService
from ..interfaces.users_service_converter import IUsersServiceConverter


class UsersService(IUsersService):
    def __init__(
        self,
        repository: IUsersRepository,
        converter: IUsersServiceConverter,
        password_hasher: IPasswordHasher,
    ):
        self._users_repository = repository
        self._password_hasher = password_hasher
        self._users_service_converter = converter

    async def get_users_list(self, users_query: IUsersQuery) -> list[IUser]:
        users_query_result = await self._users_repository.get_users(users_query)
        return self._users_service_converter.from_users_query_result(users_query_result)

    async def add_user(self, add_user_command: IAddUserCommand) -> UUID:
        password_hash = await self._password_hasher.hash(add_user_command.password)
        user_data = self._users_service_converter.to_user_data(add_user_command, password_hash, is_active=True)
        return await self._users_repository.add_user(user_data)

    async def remove_user(self, remove_user_command: IRemoveUserCommand) -> None:
        return await self._users_repository.remove_user(remove_user_command)
