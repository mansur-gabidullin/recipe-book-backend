from typing import Protocol, runtime_checkable
from uuid import UUID

from .profile_entity import IProfileEntity


@runtime_checkable
class IUserEntity(Protocol):
    uuid: UUID
    login: str
    password_hash: str
    is_removed: bool
    is_active: bool
    profile: IProfileEntity | None
