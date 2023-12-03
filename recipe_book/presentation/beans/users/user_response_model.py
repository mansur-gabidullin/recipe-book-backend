from uuid import UUID

from dataclasses import dataclass

from ...interfaces.users.user_response_model import IUserResponseModel
from .profile_response_model import ProfileResponseModel


@dataclass
class UserResponseModel(IUserResponseModel):
    uuid: UUID
    login: str
    profile: ProfileResponseModel = None
    is_active: bool = False
    is_removed: bool = False
