from uuid import UUID

from dataclasses import dataclass

from application_core.users.interfaces.user_record import IUserRecord

from infrastructure.beans.profile_result import ProfileResult


@dataclass
class UserRecord(IUserRecord):
    uuid: UUID
    login: str
    password_hash: str
    is_removed: bool
    is_active: bool
    profile: ProfileResult = None
