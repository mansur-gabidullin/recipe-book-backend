from typing import Protocol, runtime_checkable
from uuid import UUID

from application_core.users.interfaces.user import IUser

from .new_user_response import INewUserResponse
from .users_list_response import IUsersListResponse


@runtime_checkable
class IUsersConverter(Protocol):
    def from_users(self, users: list[IUser]) -> IUsersListResponse:
        ...

    def from_new_user(self, uuid: UUID) -> INewUserResponse:
        ...
