from typing import Protocol, runtime_checkable

from sqlalchemy import Result


@runtime_checkable
class IUsersInfrastructureConverter(Protocol):
    def from_users_results(self, results: Result):
        ...
