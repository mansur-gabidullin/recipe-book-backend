from typing import Protocol, runtime_checkable


@runtime_checkable
class IAddUserCommand(Protocol):
    login: str
    password: str
    password_confirm: str
    email: str
    name: str | None
    nickname: str | None
    surname: str | None
    patronymic: str | None
