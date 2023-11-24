from typing import Protocol, runtime_checkable


@runtime_checkable
class IProductsQuery(Protocol):
    limit: int | None
    is_removed: bool = False
