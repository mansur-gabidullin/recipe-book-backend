from typing import Protocol

from ..beans.dtos.user import UserDTO
from ..beans.queries.users import UsersQuery


class IUsersController(Protocol):
    async def get_users_list(self, query: UsersQuery) -> list[UserDTO]:
        ...


class IAdministratorUseCase(Protocol):
    async def fetch_users(self, query: UsersQuery) -> list[UserDTO]:
        ...
