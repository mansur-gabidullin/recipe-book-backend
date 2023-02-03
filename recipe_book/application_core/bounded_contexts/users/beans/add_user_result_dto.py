from pydantic import BaseModel


class AddUserResultDTO(BaseModel):
    id: int
