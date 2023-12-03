from typing import runtime_checkable, Protocol

from .change_product_command import IChangeProductCommand
from .product_entity import IProductEntity
from .product_record import IProductRecord
from .product_data import IProductData
from .add_product_command import IAddProductCommand


@runtime_checkable
class IProductsServiceConverter(Protocol):
    def from_record(self, record: IProductRecord) -> IProductEntity:
        ...

    def from_records(self, records: list[IProductRecord]) -> list[IProductEntity]:
        ...

    def to_product_data(self, data: IAddProductCommand | IChangeProductCommand) -> IProductData:
        ...
