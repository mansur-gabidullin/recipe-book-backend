from uuid import UUID

from dataclasses import dataclass

from application_core.users.interfaces.profile_result import IProfileRecord


@dataclass
class ProfileRecord(IProfileRecord):
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
