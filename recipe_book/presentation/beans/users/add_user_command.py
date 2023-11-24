from typing import Annotated

from pydantic import EmailStr, model_validator, StringConstraints
from dataclasses import dataclass

from constants import (
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
    login: Annotated[str, StringConstraints(min_length=USER_LOGIN_MIN_LENGTH, max_length=USER_LOGIN_MAX_LENGTH)]
    password: Annotated[str, StringConstraints(min_length=USER_PASSWORD_MIN_LENGTH)]
    password_confirm: Annotated[str, StringConstraints(min_length=USER_PASSWORD_MIN_LENGTH)]
    email: EmailStr
    phone_number: Annotated[
        str | None,
        StringConstraints(min_length=USER_PHONE_NUMBER_MIN_LENGTH, max_length=USER_PHONE_NUMBER_MAX_LENGTH),
    ] = None
    name: Annotated[
        str | None, StringConstraints(min_length=USER_NAME_MIN_LENGTH, max_length=USER_NAME_MAX_LENGTH)
    ] = None
    nickname: Annotated[
        str | None,
        StringConstraints(min_length=USER_NICKNAME_MIN_LENGTH, max_length=USER_NICKNAME_MAX_LENGTH),
    ] = None
    surname: Annotated[
        str | None,
        StringConstraints(min_length=USER_SURNAME_MIN_LENGTH, max_length=USER_SURNAME_MAX_LENGTH),
    ] = None
    patronymic: Annotated[
        str | None,
        StringConstraints(min_length=USER_PATRONYMIC_MIN_LENGTH, max_length=USER_PATRONYMIC_MAX_LENGTH),
    ] = None

    @model_validator(mode="after")
    def passwords_match(self) -> "AddUserCommand":
        password = self.password
        password_confirm = self.password_confirm
        if password is not None and password_confirm is not None and password != password_confirm:
            raise ValueError("passwords do not match")
        return self
