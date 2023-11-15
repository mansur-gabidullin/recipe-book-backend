from ..interfaces.bin_repository import IBinRestoreRepository
from ..interfaces.bin_service import IBinRestoreService


class BinRestoreService[T](IBinRestoreService[T]):
    def __init__(
        self,
        repository: IBinRestoreRepository[T],
    ):
        self._users_repository = repository

    async def restore(self, command):
        await self._users_repository.restore(command.uuid)
