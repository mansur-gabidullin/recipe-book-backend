from typing import runtime_checkable, Protocol


@runtime_checkable
class IProductData(Protocol):
    name: str
    description: str | None
    image_url: str | None
