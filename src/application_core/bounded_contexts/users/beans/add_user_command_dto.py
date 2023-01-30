from pydantic import BaseModel


class AddUserCommandDTO(BaseModel):
    login: str
    email: str | None
