from typing import Protocol
from uuid import UUID

from ..beans.user_po import UserPO
from ..beans.queries.users_query_dto import UsersQueryDTO
from ..aggregates.user import UserEntity


class IUsersRepository(Protocol):
    async def get_users(self, query: UsersQueryDTO) -> list[UserEntity]:
        ...

    async def add_user(self, user: UserPO) -> UUID:
        ...

    async def remove_user(self, uuid: UUID) -> None:
        ...


class IPasswordHasher(Protocol):
    async def hash(self, password: str) -> str:
        ...

    async def verify(self, hash_: str, password: str) -> bool:
        ...


class IAccessTokenCreator(Protocol):
    async def create(self, data: dict) -> str:
        ...

    async def read(self, token: str) -> dict:
        ...
