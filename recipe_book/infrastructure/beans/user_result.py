from uuid import UUID

from dataclasses import dataclass

from application_core.users.interfaces.user_result import IUserResult

from infrastructure.beans.profile_result import ProfileResult


@dataclass
class UserResult(IUserResult):
    uuid: UUID
    login: str
    password_hash: str
    is_removed: bool
    is_active: bool
    profile: ProfileResult = None
