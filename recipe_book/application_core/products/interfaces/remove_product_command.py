from typing import Protocol, runtime_checkable
from uuid import UUID


@runtime_checkable
class IRemoveProductCommand(Protocol):
    uuid: UUID
