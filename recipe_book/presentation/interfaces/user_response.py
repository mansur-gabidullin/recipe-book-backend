from typing import Protocol, runtime_checkable
from uuid import UUID

from .profile_response import IProfileResponse


@runtime_checkable
class IUserResponse(Protocol):
    uuid: UUID
    login: str
    is_removed: bool
    is_active: bool
    profile: IProfileResponse | None
