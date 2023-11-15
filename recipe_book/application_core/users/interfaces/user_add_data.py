from typing import Protocol, runtime_checkable


@runtime_checkable
class IAddUserData(Protocol):
    is_active: bool
    login: str
    password_hash: str
    email: str
    phone_number: str | None
    name: str | None
    nickname: str | None
    surname: str | None
    patronymic: str | None
