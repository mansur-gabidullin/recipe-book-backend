from typing import Protocol, runtime_checkable

from .add_user_command import IAddUserCommand
from .user import IUser
from .user_data import IUserData
from .user_result import IUserResult


@runtime_checkable
class IUsersServiceConverter(Protocol):
    def from_users_query_result(self, users: list[IUserResult]) -> list[IUser]:
        ...

    def to_user_data(
        self, add_user_command: IAddUserCommand, password_hash: str, *, is_active: bool = True
    ) -> IUserData:
        ...
