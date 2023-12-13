from typing import Protocol, runtime_checkable
from uuid import UUID


@runtime_checkable
class IProductEntity(Protocol):
    uuid: UUID
    name: str
    description: str | None
    image_url: str | None
