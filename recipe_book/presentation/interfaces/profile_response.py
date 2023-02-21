from typing import Protocol, runtime_checkable


@runtime_checkable
class IProfileResponse(Protocol):
    email: str
    name: str | None
    nickname: str | None
    surname: str | None
    patronymic: str | None