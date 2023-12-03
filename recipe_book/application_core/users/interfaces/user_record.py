from typing import Protocol, runtime_checkable
from uuid import UUID

from .profile_result import IProfileRecord


@runtime_checkable
class IUserRecord(Protocol):
    uuid: UUID
    login: str
    password_hash: str
    profile: IProfileRecord | None
    is_active: bool
    is_removed: bool
