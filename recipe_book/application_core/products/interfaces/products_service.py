from typing import runtime_checkable, Protocol
from uuid import UUID

from .add_product_command import IAddProductCommand
from .change_product_command import IChangeProductCommand
from .product_entity import IProductEntity
from .product_query import IProductQuery
from .products_query import IProductsQuery
from .remove_product_command import IRemoveProductCommand


@runtime_checkable
class IProductsService(Protocol):
    async def get_product(self, query: IProductQuery) -> IProductEntity | None:
        ...

    async def get_products(self, query: IProductsQuery) -> list[IProductEntity]:
        ...

    async def add_product(self, command: IAddProductCommand) -> UUID:
        ...

    async def update_product(self, uuid: UUID, command: IChangeProductCommand) -> IProductEntity:
        ...

    async def delete_product(self, command: IRemoveProductCommand) -> None:
        ...
