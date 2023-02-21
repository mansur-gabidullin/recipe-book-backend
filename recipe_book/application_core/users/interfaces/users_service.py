from typing import Protocol, runtime_checkable
from uuid import UUID

from .add_user_command import IAddUserCommand
from .remove_user_command import IRemoveUserCommand
from .users_query import IUsersQuery
from .user import IUser


@runtime_checkable
class IUsersService(Protocol):
    async def get_users_list(self, users_query: IUsersQuery) -> list[IUser]:
        ...

    async def add_user(self, add_user_command: IAddUserCommand) -> UUID:
        ...

    async def remove_user(self, remove_user_command: IRemoveUserCommand) -> None:
        ...
