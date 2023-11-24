from uuid import UUID

from dataclasses import dataclass

from ...interfaces.users.user_response_model import IUserResponseModel
from .profile_response_model import ProfileResponseModel


@dataclass
class UserResponseModel(IUserResponseModel):
    uuid: UUID
    login: str
    is_removed: bool
    is_active: bool
    profile: ProfileResponseModel = None
