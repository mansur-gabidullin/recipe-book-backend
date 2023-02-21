from typing import Protocol, runtime_checkable


@runtime_checkable
class IUserData(Protocol):
    is_active: bool
    login: str
    password_hash: str
    email: str
    name: str | None
    nickname: str | None
    surname: str | None
    patronymic: str | None
