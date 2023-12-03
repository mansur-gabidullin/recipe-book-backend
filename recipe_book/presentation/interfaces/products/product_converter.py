from typing import runtime_checkable, Protocol
from uuid import UUID

from application_core.products.interfaces.product_entity import IProductEntity
from .new_product_response_model import INewProductResponseModel
from .product_response_model import IProductResponseModel


@runtime_checkable
class IProductResponseConverter(Protocol):
    def from_entity(self, product: IProductEntity) -> IProductResponseModel:
        ...

    def from_entities(self, products: list[IProductEntity]) -> list[IProductResponseModel]:
        ...

    def from_new_product(self, uuid: UUID) -> INewProductResponseModel:
        ...
