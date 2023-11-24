from uuid import UUID

from dataclasses import dataclass

from application_core.bin.interfaces.bin_action import IBinAction
from application_core.bin.interfaces.bin_restore_command import IBinCommand


@dataclass
class BinCommand(IBinCommand):
    uuid: UUID
    action: IBinAction
