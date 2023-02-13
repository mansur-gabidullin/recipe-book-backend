from pydantic import BaseModel


class UserPO(BaseModel):
    login: str
    password_hash: str
    is_active: bool
    email: str = None
    verified_email: str = None
    name: str = None
    nickname: str = None
    surname: str = None
    patronymic: str = None
