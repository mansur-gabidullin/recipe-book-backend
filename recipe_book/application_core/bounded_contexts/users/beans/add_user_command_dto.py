from pydantic import BaseModel, EmailStr


class AddUserCommandDTO(BaseModel):
    login: str
    email: EmailStr = None
