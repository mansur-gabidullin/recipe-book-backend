from typing import Protocol, runtime_checkable


@runtime_checkable
class IUsersQuery(Protocol):
    login: str | None
    limit: int | None
    is_removed: bool
