from uuid import UUID

from pydantic import BaseModel

from infrastructure.beans.profile_result import ProfileResult


# from application_core.users.interfaces.user_result import IUserResult
# from application_core.users.interfaces.profile_result import IProfileResult


class UserResult(BaseModel):
    uuid: UUID
    login: str
    password_hash: str
    is_removed: bool
    is_active: bool
    profile: ProfileResult = None
