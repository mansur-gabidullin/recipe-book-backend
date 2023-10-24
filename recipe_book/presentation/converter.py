from uuid import UUID

from application_core.users.interfaces.user import IUser

from .beans.new_user_response import NewUserResponse
from .beans.profile_response import ProfileResponse
from .beans.user_response import UserResponse

from .interfaces.new_user_response import INewUserResponse
from .interfaces.user_response import IUserResponse
from .interfaces.users_converter import IUsersPresentationConverter


class UsersPresentationConverter(IUsersPresentationConverter):
    def from_users(self, users: list[IUser]) -> list[IUserResponse]:
        return [
            UserResponse(
                uuid=user.uuid,
                login=user.login,
                is_removed=user.is_removed,
                is_active=user.is_active,
                profile=ProfileResponse(
                    email=user.profile.email,
                    phone_number=user.profile.phone_number,
                    name=user.profile.name,
                    nickname=user.profile.nickname,
                    surname=user.profile.surname,
                    patronymic=user.profile.patronymic,
                )
                if user.profile
                else None,
            )
            for user in users
        ]

    def from_new_user(self, uuid: UUID) -> INewUserResponse:
        return NewUserResponse(uuid=uuid)
