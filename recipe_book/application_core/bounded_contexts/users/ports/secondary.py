from typing import Protocol
from uuid import UUID

from ..beans.user_po import UserPO
from ..beans.queries.users_query_dto import UsersQueryDTO
from ..entities.user import UserEntity


class IUsersRepository(Protocol):
    async def get_users(self, query: UsersQueryDTO) -> list[UserEntity]:
        ...

    async def add_user(self, user: UserPO) -> UUID:
        ...
