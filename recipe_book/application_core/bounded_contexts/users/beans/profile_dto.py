from uuid import UUID

from pydantic import BaseModel


class ProfileDTO(BaseModel):
    uuid: UUID
    user_uuid: UUID
    email: str
    verified_email: str = None
    name: str = None
    nickname: str = None
    surname: str = None
    patronymic: str = None
