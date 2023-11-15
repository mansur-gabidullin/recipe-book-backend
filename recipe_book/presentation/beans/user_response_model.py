from uuid import UUID

from dataclasses import dataclass

from .profile_response_model import ProfileResponseModel
from ..interfaces.user_response_model import IUserResponseModel


@dataclass
class UserResponseModel(IUserResponseModel):
    uuid: UUID
    login: str
    is_removed: bool
    is_active: bool
    profile: ProfileResponseModel = None
