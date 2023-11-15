from typing import Protocol, runtime_checkable
from uuid import UUID

from application_core.users.interfaces.profile import IProfile


@runtime_checkable
class IUserEntity(Protocol):
    uuid: UUID
    login: str
    password_hash: str
    is_removed: bool
    is_active: bool
    profile: IProfile | None
