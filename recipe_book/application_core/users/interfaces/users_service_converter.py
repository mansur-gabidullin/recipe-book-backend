from typing import Protocol, runtime_checkable

from .add_user_command import IAddUserCommand
from .user_entity import IUserEntity
from .user_data import IUserData
from .user_record import IUserRecord


@runtime_checkable
class IUsersServiceConverter(Protocol):
    def from_users_query_result(self, users: list[IUserRecord]) -> list[IUserEntity]:
        ...

    def from_user(self, users: IUserRecord) -> IUserEntity:
        ...

    def to_user_data(
        self, add_user_command: IAddUserCommand, password_hash: str, *, is_active: bool = True
    ) -> IUserData:
        ...
