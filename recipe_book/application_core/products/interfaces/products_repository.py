from typing import runtime_checkable, Protocol
from uuid import UUID

from .product_data import IProductData
from .product_query import IProductQuery
from .product_record import IProductRecord
from .products_query import IProductsQuery
from .remove_product_command import IRemoveProductCommand


@runtime_checkable
class IProductsRepository(Protocol):
    async def get_product(self, query: IProductQuery) -> IProductRecord | None:
        ...

    async def get_products(self, query: IProductsQuery) -> list[IProductRecord]:
        ...

    async def add_product(self, data: IProductData) -> UUID:
        ...

    async def update_product(self, uuid: UUID, data: IProductData) -> IProductRecord:
        ...

    async def remove_product(self, command: IRemoveProductCommand) -> None:
        ...

    async def delete_product(self, command: IRemoveProductCommand) -> None:
        ...
