from .aggregates.profile import ProfileEntity
from .aggregates.user import UserEntityEntity
from .beans.add_user_data import AddUserData
from .interfaces.add_user_command import IAddUserCommand
from .interfaces.user_entity import IUserEntity
from .interfaces.user_add_data import IAddUserData
from .interfaces.user_record import IUserRecord
from .interfaces.user_converter import IUserEntityConverter


class UserEntityConverter(IUserEntityConverter):
    def from_user(self, user: IUserRecord) -> IUserEntity:
        return UserEntityEntity(
            uuid=user.uuid,
            login=user.login,
            password_hash=user.password_hash,
            is_removed=user.is_removed,
            is_active=user.is_active,
            profile=ProfileEntity(
                uuid=user.profile.uuid,
                user_uuid=user.profile.user_uuid,
                email=user.profile.email,
                verified_email=user.profile.verified_email,
                verified_phone_number=user.profile.verified_phone_number,
                name=user.profile.name,
                nickname=user.profile.nickname,
                surname=user.profile.surname,
                patronymic=user.profile.patronymic,
            )
            if user.profile
            else None,
        )

    def from_users_query_result(self, users: list[IUserRecord]) -> list[IUserEntity]:
        return [self.from_user(user) for user in users]

    def to_add_user_data(
        self, add_user_command: IAddUserCommand, password_hash: str, *, is_active: bool = True
    ) -> IAddUserData:
        return AddUserData(
            is_active=is_active,
            password_hash=password_hash,
            login=add_user_command.login,
            email=add_user_command.email,
            name=add_user_command.name,
            nickname=add_user_command.nickname,
            surname=add_user_command.surname,
            patronymic=add_user_command.patronymic,
        )
