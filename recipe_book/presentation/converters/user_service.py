from uuid import UUID

from application_core.users.interfaces.user import IUser

from ..beans.new_user_response import NewUserResponse
from ..interfaces.new_user_response import INewUserResponse
from ..interfaces.users_converter import IUsersConverter
from ..interfaces.users_list_response import IUsersListResponse


class UsersConverter(IUsersConverter):
    def from_users(self, users: list[IUser]) -> IUsersListResponse:
        return users

    def from_new_user(self, uuid: UUID) -> INewUserResponse:
        return NewUserResponse(uuid=uuid)
