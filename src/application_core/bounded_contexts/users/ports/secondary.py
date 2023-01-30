from typing import Protocol

from ..beans.dtos.user import UserDTO
from ..beans.queries.users import UsersQuery


class IUsersRepository(Protocol):
    async def get_users(self, query: UsersQuery) -> list[UserDTO]:
        ...
