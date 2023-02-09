from dataclasses import dataclass
from uuid import UUID

_solt: str = "0"
_hash: str = "0"


@dataclass
class UserEntity:
    uuid: UUID
    login: str
    password_solt: str
    password_hash: str
    email: str = None

    @classmethod
    def generate_password(cls) -> tuple[str, str]:
        return str(int(_solt) + 1), str(int(_hash) + 1)
