from uuid import UUID

from pydantic import BaseModel


class NewUserResponse(BaseModel):  # implements INewUserResponse
    uuid: UUID
