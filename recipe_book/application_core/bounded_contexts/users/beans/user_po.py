from pydantic import BaseModel


class UserPO(BaseModel):
    login: str
    password_solt: str
    password_hash: str
    email: str = None
