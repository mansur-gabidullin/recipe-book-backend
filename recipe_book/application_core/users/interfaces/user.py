from typing import Protocol, runtime_checkable
from uuid import UUID

from application_core.users.interfaces.profile import IProfile


@runtime_checkable
class IUser(Protocol):
    uuid: UUID
    login: str
    is_removed: bool
    is_active: bool
    profile: IProfile | None
