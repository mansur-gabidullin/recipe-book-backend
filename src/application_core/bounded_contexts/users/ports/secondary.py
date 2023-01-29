from typing import Protocol

from sqlalchemy.ext.asyncio import AsyncSession

from ..beans.dtos.user import UserDTO
from ..beans.queries.users_list import UsersListQuery

IDatabaseSession = AsyncSession


class IUsersRepository(Protocol):
    async def get_users_list(self, query: UsersListQuery) -> list[UserDTO]:
        ...
