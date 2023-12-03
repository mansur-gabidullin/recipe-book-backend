from typing import runtime_checkable, Protocol


@runtime_checkable
class IDictionaryItemResponseModel(Protocol):
    code: str
    title: str
