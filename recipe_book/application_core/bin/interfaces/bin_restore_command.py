from typing import Protocol, runtime_checkable
from uuid import UUID

from application_core.bin.interfaces.bin_action import IBinAction


@runtime_checkable
class IBinCommand(Protocol):
    uuid: UUID
    action: IBinAction
