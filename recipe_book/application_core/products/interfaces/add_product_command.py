from typing import runtime_checkable, Protocol


@runtime_checkable
class IAddProductCommand(Protocol):
    name: str
    description: str | None
    image_url: str | None
