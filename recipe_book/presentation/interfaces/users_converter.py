from typing import Protocol, runtime_checkable
from uuid import UUID

from application_core.users.interfaces.user import IUser

from .new_user_response import INewUserResponse
from .user_response import IUserResponse


@runtime_checkable
class IUsersPresentationConverter(Protocol):
    def from_users(self, users: list[IUser]) -> list[IUserResponse]:
        ...

    def from_new_user(self, uuid: UUID) -> INewUserResponse:
        ...
