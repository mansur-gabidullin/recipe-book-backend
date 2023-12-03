from typing import runtime_checkable, Protocol
from uuid import UUID


@runtime_checkable
class IProductRecord(Protocol):
    uuid: UUID
    name: str
    description: str | None
    image_url: str | None
    is_removed: bool
