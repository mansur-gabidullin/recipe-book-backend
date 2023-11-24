from dataclasses import dataclass

from ...interfaces.users.profile_response_model import IProfileResponseModel


@dataclass
class ProfileResponseModel(IProfileResponseModel):
    email: str
    phone_number: str = None
    name: str = None
    nickname: str = None
    surname: str = None
    patronymic: str = None
