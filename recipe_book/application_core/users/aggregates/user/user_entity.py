from dataclasses import dataclass
from uuid import UUID

from ...interfaces.user_entity import IUserEntity

from .profile_entity import ProfileEntity


@dataclass
class UserEntity(IUserEntity):
    uuid: UUID
    login: str
    password_hash: str
    is_removed: bool
    is_active: bool
    profile: ProfileEntity = None
