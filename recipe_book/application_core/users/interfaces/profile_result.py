from typing import Protocol, runtime_checkable
from uuid import UUID


@runtime_checkable
class IProfileResult(Protocol):
    uuid: UUID
    user_uuid: UUID
    email: str
    verified_email: str | None
    verified_phone_number: str | None
    phone_number: str | None
    name: str | None
    nickname: str | None
    surname: str | None
    patronymic: str | None
