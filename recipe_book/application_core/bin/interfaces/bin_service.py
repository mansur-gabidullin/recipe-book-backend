from typing import Protocol, runtime_checkable

from .bin_restore_command import IBinCommand


@runtime_checkable
class IBinService[T](Protocol):
    async def restore(self, command: IBinCommand):
        ...
