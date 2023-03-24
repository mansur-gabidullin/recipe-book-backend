from uuid import UUID

from application_core.users.interfaces.user import IUser

from .beans.new_user_response import NewUserResponse

from .interfaces.new_user_response import INewUserResponse
from .interfaces.user_response import IUserResponse
from .interfaces.users_converter import IUsersPresentationConverter


class UsersPresentationConverter(IUsersPresentationConverter):
    def from_users(self, users: list[IUser]) -> list[IUserResponse]:
        return users

    def from_new_user(self, uuid: UUID) -> INewUserResponse:
        return NewUserResponse(uuid=uuid)
