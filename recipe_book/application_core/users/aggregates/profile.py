from dataclasses import dataclass
from uuid import UUID

from application_core.users.interfaces.profile import IProfile


@dataclass
class ProfileEntity(IProfile):
    uuid: UUID
    user_uuid: UUID
    email: str
    verified_email: str = None
    name: str = None
    nickname: str = None
    surname: str = None
    patronymic: str = None
