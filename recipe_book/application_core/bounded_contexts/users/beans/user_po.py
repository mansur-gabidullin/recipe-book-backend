from pydantic import BaseModel


class UserPO(BaseModel):
    login: str
    password_hash: str
    email: str = None
    name: str = None
    nickname: str = None
    surname: str = None
    patronymic: str = None
