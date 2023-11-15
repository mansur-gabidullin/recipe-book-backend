from typing import Protocol, runtime_checkable

from .user_restore_command import IUserRestoreCommand


@runtime_checkable
class IBinService[T](Protocol):
    async def restore(self, command: IUserRestoreCommand):
        ...
