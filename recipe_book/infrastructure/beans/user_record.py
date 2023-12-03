from uuid import UUID

from dataclasses import dataclass

from application_core.users.interfaces.user_record import IUserRecord

from .profile_record import ProfileRecord


@dataclass
class UserRecord(IUserRecord):
    uuid: UUID
    login: str
    password_hash: str
    profile: ProfileRecord = None
    is_active: bool = False
    is_removed: bool = False
