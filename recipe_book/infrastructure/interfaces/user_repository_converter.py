from typing import Protocol, runtime_checkable

from sqlalchemy import Result

from application_core.users.interfaces.user_record import IUserRecord


@runtime_checkable
class IUserRepositoryConverter(Protocol):
    def from_query_results(self, results: Result) -> list[IUserRecord]:
        ...
