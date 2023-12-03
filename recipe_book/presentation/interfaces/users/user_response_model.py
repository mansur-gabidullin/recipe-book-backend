from typing import Protocol, runtime_checkable
from uuid import UUID

from .profile_response_model import IProfileResponseModel


@runtime_checkable
class IUserResponseModel(Protocol):
    uuid: UUID
    login: str
    profile: IProfileResponseModel | None
    is_removed: bool
    is_active: bool
