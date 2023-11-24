from typing import runtime_checkable, Protocol
from uuid import UUID

from .product_data import IProductData


@runtime_checkable
class IProductsRepository(Protocol):
    async def add_product(self, data: IProductData) -> UUID:
        ...
