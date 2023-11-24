from typing import runtime_checkable, Protocol

from .product_data import IProductData
from .add_product_command import IAddProductCommand


@runtime_checkable
class IProductsServiceConverter(Protocol):
    def to_product_data(self, data: IAddProductCommand) -> IProductData:
        ...
