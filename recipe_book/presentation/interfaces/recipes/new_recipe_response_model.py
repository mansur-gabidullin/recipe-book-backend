from typing import runtime_checkable, Protocol
from uuid import UUID


@runtime_checkable
class INewRecipeResponseModel(Protocol):
    uuid: UUID
