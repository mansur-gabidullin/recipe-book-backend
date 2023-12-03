from typing import Protocol, runtime_checkable
from uuid import UUID

from .profile_entity import IProfileEntity


@runtime_checkable
class IUserEntity(Protocol):
    uuid: UUID
    login: str
    password_hash: str
    profile: IProfileEntity | None
    is_active: bool
    is_removed: bool
