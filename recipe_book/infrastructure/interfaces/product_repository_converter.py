from typing import runtime_checkable, Protocol

from sqlalchemy import Result

from application_core.products.interfaces.product_record import IProductRecord


@runtime_checkable
class IProductRepositoryConverter(Protocol):
    def from_query_results(self, results: Result) -> list[IProductRecord]:
        ...
