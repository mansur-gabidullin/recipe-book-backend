from ..interfaces.bin_repository import IBinRepository
from ..interfaces.bin_service import IBinService


class UsersBinService[T](IBinService[T]):
    def __init__(
        self,
        repository: IBinRepository[T],
    ):
        self._users_repository = repository

    async def restore(self, command):
        await self._users_repository.restore(command.uuid)
