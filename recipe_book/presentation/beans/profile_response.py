from pydantic import BaseModel


class ProfileResponse(BaseModel):  # implements IProfileResponse
    email: str
    name: str = None
    nickname: str = None
    surname: str = None
    patronymic: str = None
