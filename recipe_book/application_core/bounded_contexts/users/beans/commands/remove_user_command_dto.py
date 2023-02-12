from uuid import UUID

from pydantic import BaseModel


class RemoveUserCommandDTO(BaseModel):
    uuid: UUID
