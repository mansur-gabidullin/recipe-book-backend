from uuid import UUID

from pydantic import BaseModel


class RegisterUserResultDTO(BaseModel):
    uuid: UUID
