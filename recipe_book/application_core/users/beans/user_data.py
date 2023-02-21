from pydantic import BaseModel


class UserData(BaseModel):  # implements IUserData
    is_active: bool
    login: str
    password_hash: str
    email: str
    name: str = None
    nickname: str = None
    surname: str = None
    patronymic: str = None
