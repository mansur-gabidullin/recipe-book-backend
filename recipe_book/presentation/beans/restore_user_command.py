from uuid import UUID

from dataclasses import dataclass

from application_core.bin.interfaces.user_restore_command import IUserRestoreCommand


@dataclass
class UserRestoreCommand(IUserRestoreCommand):
    uuid: UUID
