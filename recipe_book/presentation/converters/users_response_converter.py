from application_core.users.interfaces.user_entity import IUserEntity

from ..interfaces.users.user_response_model import IUserResponseModel
from ..interfaces.users.user_converter import IUserResponseConverter

from ..beans.users.new_user_response_model import NewUserResponseModel
from ..beans.users.profile_response_model import ProfileResponseModel
from ..beans.users.user_response_model import UserResponseModel


class UserResponseConverter(IUserResponseConverter):
    def from_entities(self, users: list[IUserEntity]) -> list[IUserResponseModel]:
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

    def from_new_user(self, uuid):
        return NewUserResponseModel(uuid=uuid)
