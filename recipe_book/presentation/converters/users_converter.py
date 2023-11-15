from uuid import UUID

from application_core.users.interfaces.user_entity import IUserEntity

from ..interfaces.new_user_response_model import INewUserResponseModel
from ..interfaces.user_response_model import IUserResponseModel
from ..interfaces.user_converter import IUserResponseConverter

from ..beans.new_user_response_model import NewUserResponseModel
from ..beans.profile_response_model import ProfileResponseModel
from ..beans.user_response_model import UserResponseModel


class UserResponseConverter(IUserResponseConverter):
    def from_users(self, users: list[IUserEntity]) -> list[IUserResponseModel]:
        return [
            UserResponseModel(
                uuid=user.uuid,
                login=user.login,
                is_removed=user.is_removed,
                is_active=user.is_active,
                profile=ProfileResponseModel(
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

    def from_new_user(self, uuid: UUID) -> INewUserResponseModel:
        return NewUserResponseModel(uuid=uuid)
