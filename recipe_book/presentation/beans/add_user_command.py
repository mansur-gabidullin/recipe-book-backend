from pydantic import EmailStr, constr, validator
from dataclasses import dataclass

from application_core.users.constants import (
    USER_LOGIN_MIN_LENGTH,
    USER_LOGIN_MAX_LENGTH,
    USER_NICKNAME_MIN_LENGTH,
    USER_NICKNAME_MAX_LENGTH,
    USER_NAME_MIN_LENGTH,
    USER_NAME_MAX_LENGTH,
    USER_PHONE_NUMBER_MIN_LENGTH,
    USER_PHONE_NUMBER_MAX_LENGTH,
    USER_SURNAME_MIN_LENGTH,
    USER_SURNAME_MAX_LENGTH,
    USER_PATRONYMIC_MIN_LENGTH,
    USER_PATRONYMIC_MAX_LENGTH,
    USER_PASSWORD_MIN_LENGTH,
)
from application_core.users.interfaces.add_user_command import IAddUserCommand


@dataclass
class AddUserCommand(IAddUserCommand):
    login: constr(min_length=USER_LOGIN_MIN_LENGTH, max_length=USER_LOGIN_MAX_LENGTH)
    password: constr(min_length=USER_PASSWORD_MIN_LENGTH)
    password_confirm: constr(min_length=USER_PASSWORD_MIN_LENGTH)
    email: EmailStr
    phone_number: constr(min_length=USER_PHONE_NUMBER_MIN_LENGTH, max_length=USER_PHONE_NUMBER_MAX_LENGTH) = None
    name: constr(min_length=USER_NAME_MIN_LENGTH, max_length=USER_NAME_MAX_LENGTH) = None
    nickname: constr(min_length=USER_NICKNAME_MIN_LENGTH, max_length=USER_NICKNAME_MAX_LENGTH) = None
    surname: constr(min_length=USER_SURNAME_MIN_LENGTH, max_length=USER_SURNAME_MAX_LENGTH) = None
    patronymic: constr(min_length=USER_PATRONYMIC_MIN_LENGTH, max_length=USER_PATRONYMIC_MAX_LENGTH) = None

    @validator("password_confirm")
    def passwords_match(cls, field_value, values, **kwargs):
        if "password" in values and field_value != values["password"]:
            raise ValueError("passwords do not match")
        return field_value
