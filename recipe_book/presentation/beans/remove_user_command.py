from uuid import UUID

from dataclasses import dataclass

from application_core.users.interfaces.remove_user_command import IRemoveUserCommand


@dataclass
class RemoveUserCommand(IRemoveUserCommand):
    uuid: UUID
