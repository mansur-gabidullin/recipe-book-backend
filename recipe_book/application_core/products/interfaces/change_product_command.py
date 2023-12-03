from typing import Protocol, runtime_checkable


@runtime_checkable
class IChangeProductCommand(Protocol):
    name: str
    description: str | None
    image_url: str | None
