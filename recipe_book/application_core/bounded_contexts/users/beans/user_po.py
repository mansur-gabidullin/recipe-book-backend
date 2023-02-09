from pydantic import BaseModel, EmailStr


class UserPO(BaseModel):
    login: str
    password_solt: str
    password_hash: str
    email: EmailStr = None
