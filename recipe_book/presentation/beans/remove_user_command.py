from uuid import UUID

from pydantic import BaseModel


class RemoveUserCommand(BaseModel):  # implements IRemoveUserCommand
    uuid: UUID
