from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    login: str
    email: str = None
