from typing import Protocol

from beans.dtos.user import UserDTO
from beans.queries.users_list import UsersListQuery


class IUsersController(Protocol):
    async def get_users_list(self, query: UsersListQuery) -> list[UserDTO]:
        ...


class IUsersService(Protocol):
    async def execute(self, query: UsersListQuery) -> list[UserDTO]:
        ...
