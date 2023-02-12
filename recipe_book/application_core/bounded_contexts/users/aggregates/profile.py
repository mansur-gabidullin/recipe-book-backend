from dataclasses import dataclass
from uuid import UUID


@dataclass
class ProfileEntity:
    uuid: UUID
    user_uuid: UUID
    email: str
    verified_email: str = None
    name: str = None
    nickname: str = None
    surname: str = None
    patronymic: str = None
