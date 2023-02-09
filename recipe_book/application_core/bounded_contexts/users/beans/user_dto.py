from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserDTO(BaseModel):
    uuid: UUID
    login: str
    email: EmailStr = None
