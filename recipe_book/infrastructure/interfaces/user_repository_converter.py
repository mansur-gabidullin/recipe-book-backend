from typing import Protocol, runtime_checkable

from sqlalchemy import Result


@runtime_checkable
class IUserRepositoryConverter(Protocol):
    def from_users_results(self, results: Result):
        ...
