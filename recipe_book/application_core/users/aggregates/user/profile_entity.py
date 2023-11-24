from dataclasses import dataclass
from uuid import UUID

from ...interfaces.profile_entity import IProfileEntity


@dataclass
class ProfileEntity(IProfileEntity):
    uuid: UUID
    user_uuid: UUID
    email: str
    verified_email: str = None
    phone_number: str = None
    verified_phone_number: str = None
    name: str = None
    nickname: str = None
    surname: str = None
    patronymic: str = None
