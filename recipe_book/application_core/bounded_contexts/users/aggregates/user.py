from dataclasses import dataclass
from uuid import UUID

from argon2 import PasswordHasher

from .profile import ProfileEntity


@dataclass
class UserEntity:
    uuid: UUID
    login: str
    password_hash: str
    is_removed: bool
    profile: ProfileEntity = None

    @classmethod
    def generate_password_hash(cls, password: str) -> str:
        return PasswordHasher().hash(password)
