from dataclasses import dataclass
from uuid import UUID

from argon2 import PasswordHasher


@dataclass
class UserEntity:
    uuid: UUID
    login: str
    password_hash: str
    email: str = None

    @classmethod
    def generate_password_hash(cls, password: str) -> str:
        return PasswordHasher().hash(password)
