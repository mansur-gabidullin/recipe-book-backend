from uuid import UUID

from dataclasses import dataclass

from .profile_response import ProfileResponse
from ..interfaces.user_response import IUserResponse


@dataclass
class UserResponse(IUserResponse):
    uuid: UUID
    login: str
    is_removed: bool
    is_active: bool
    profile: ProfileResponse = None
