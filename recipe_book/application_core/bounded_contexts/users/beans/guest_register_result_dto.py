from uuid import UUID

from pydantic import BaseModel


class GuestRegisterResultDTO(BaseModel):
    uuid: UUID
