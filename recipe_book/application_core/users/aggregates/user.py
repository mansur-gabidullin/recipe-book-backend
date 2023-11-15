from dataclasses import dataclass
from uuid import UUID

from .profile import ProfileEntity
from ..interfaces.user_entity import IUserEntity


@dataclass
class UserEntityEntity(IUserEntity):
    uuid: UUID
    login: str
    password_hash: str
    is_removed: bool
    is_active: bool
    profile: ProfileEntity = None
