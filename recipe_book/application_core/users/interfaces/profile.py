from typing import Protocol, runtime_checkable


@runtime_checkable
class IProfile(Protocol):
    email: str
    phone_number: str | None
    name: str | None
    nickname: str | None
    surname: str | None
    patronymic: str | None
