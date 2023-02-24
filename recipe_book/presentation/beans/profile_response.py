from dataclasses import dataclass

from presentation.interfaces.profile_response import IProfileResponse


@dataclass
class ProfileResponse(IProfileResponse):
    email: str
    phone_number: str = None
    name: str = None
    nickname: str = None
    surname: str = None
    patronymic: str = None
