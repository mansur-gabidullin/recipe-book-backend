from typing import Protocol, runtime_checkable
from uuid import UUID

from .remove_user_command import IRemoveUserCommand
from .user_add_data import IAddUserData
from .user_record import IUserRecord
from .users_query import IUsersQuery


@runtime_checkable
class IUsersRepository(Protocol):
    async def get_users(self, query_query: IUsersQuery) -> list[IUserRecord]:
        ...

    async def get_user_by_login(self, login: str) -> IUserRecord:
        ...

    async def get_user_by_uuid(self, uuid: UUID) -> IUserRecord:
        ...

    async def add_user(self, user_data: IAddUserData) -> UUID:
        ...

    async def remove_user(self, remove_user_command: IRemoveUserCommand) -> None:
        ...
