from dataclasses import dataclass
from uuid import UUID

from .profile import ProfileEntity


@dataclass
class UserEntity:
    uuid: UUID
    login: str
    password_hash: str
    is_removed: bool
    is_active: bool
    profile: ProfileEntity = None
