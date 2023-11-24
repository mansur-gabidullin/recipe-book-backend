from typing import runtime_checkable, Protocol
from uuid import UUID

from .add_product_command import IAddProductCommand
from .product_entity import IProductEntity
from .products_query import IProductsQuery


@runtime_checkable
class IProductsService(Protocol):
    async def get_products(self, products_query: IProductsQuery) -> list[IProductEntity]:
        ...

    async def add_product(self, add_product_command: IAddProductCommand) -> UUID:
        ...
