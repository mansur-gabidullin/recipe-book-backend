from typing import Protocol, runtime_checkable
from uuid import UUID


@runtime_checkable
class IBinRepository[T](Protocol):
    async def restore(self, uuid: UUID):
        ...
