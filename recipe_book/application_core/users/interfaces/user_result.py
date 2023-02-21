from typing import Protocol, runtime_checkable
from uuid import UUID

from .profile_result import IProfileResult


@runtime_checkable
class IUserResult(Protocol):
    uuid: UUID
    login: str
    password_hash: str
    is_removed: bool
    is_active: bool
    profile: IProfileResult | None
