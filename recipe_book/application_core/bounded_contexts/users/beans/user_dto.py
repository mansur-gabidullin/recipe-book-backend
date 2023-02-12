from uuid import UUID

from pydantic import BaseModel

from .profile_dto import ProfileDTO


class UserDTO(BaseModel):
    uuid: UUID
    login: str
    is_removed: bool
    profile: ProfileDTO = None
