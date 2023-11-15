from dataclasses import dataclass

from application_core.users.interfaces.user_add_data import IAddUserData


@dataclass
class AddUserData(IAddUserData):
    is_active: bool
    login: str
    password_hash: str
    email: str
    phone_number: str = None
    name: str = None
    nickname: str = None
    surname: str = None
    patronymic: str = None
