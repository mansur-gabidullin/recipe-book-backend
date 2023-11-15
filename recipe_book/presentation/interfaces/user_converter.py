from typing import Protocol, runtime_checkable
from uuid import UUID

from application_core.users.interfaces.user_entity import IUserEntity

from .new_user_response_model import INewUserResponseModel
from .user_response_model import IUserResponseModel


@runtime_checkable
class IUserResponseConverter(Protocol):
    def from_users(self, users: list[IUserEntity]) -> list[IUserResponseModel]:
        ...

    def from_new_user(self, uuid: UUID) -> INewUserResponseModel:
        ...
