from typing import runtime_checkable, Protocol
from uuid import UUID


@runtime_checkable
class INewProductResponseModel(Protocol):
    uuid: UUID
