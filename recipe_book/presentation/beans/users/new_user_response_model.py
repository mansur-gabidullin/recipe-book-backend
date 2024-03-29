from uuid import UUID

from dataclasses import dataclass

from ...interfaces.users.new_user_response_model import INewUserResponseModel


@dataclass
class NewUserResponseModel(INewUserResponseModel):
    uuid: UUID
