from uuid import UUID

from pydantic import BaseModel

from .profile_response import ProfileResponse


class UserResponse(BaseModel):  # implements IUserResponse
    uuid: UUID
    login: str
    is_removed: bool
    is_active: bool
    profile: ProfileResponse = None
