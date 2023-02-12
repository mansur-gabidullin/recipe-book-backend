from typing import Protocol, Iterable
from uuid import UUID

from ..beans.user_po import UserPO
from ..beans.queries.users_query_dto import UsersQueryDTO
from ..aggregates.user import UserEntity


class IUsersRepository(Protocol):
    async def get_users(self, query: UsersQueryDTO) -> Iterable[UserEntity]:
        ...

    async def add_user(self, user: UserPO) -> UUID:
        ...

    async def remove_user(self, uuid: UUID) -> None:
        ...
