from typing import runtime_checkable, Protocol
from uuid import UUID


@runtime_checkable
class IProductResponseModel(Protocol):
    uuid: UUID
    name: str
    description: str | None
    image_url: str | None
