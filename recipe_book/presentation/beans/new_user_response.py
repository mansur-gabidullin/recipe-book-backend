from uuid import UUID

from dataclasses import dataclass

from presentation.interfaces.new_user_response import INewUserResponse


@dataclass
class NewUserResponse(INewUserResponse):
    uuid: UUID
