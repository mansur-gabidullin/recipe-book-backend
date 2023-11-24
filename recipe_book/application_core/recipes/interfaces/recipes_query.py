from typing import Protocol, runtime_checkable


@runtime_checkable
class IRecipesQuery(Protocol):
    limit: int | None
    is_removed: bool = False
