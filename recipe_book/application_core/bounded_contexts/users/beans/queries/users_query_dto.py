from pydantic import BaseModel


class UsersQueryDTO(BaseModel):
    login: str = None
    limit: int = None
