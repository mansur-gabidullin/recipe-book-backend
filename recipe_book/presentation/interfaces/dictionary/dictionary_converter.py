from typing import Protocol, runtime_checkable

from application_core.products.interfaces.product_entity import IProductEntity

from .dictionary_item_response_model import IDictionaryItemResponseModel


@runtime_checkable
class IDictionaryResponseConverter(Protocol):
    def from_entity(self, product: IProductEntity) -> IDictionaryItemResponseModel:
        ...

    def from_entities(self, products: list[IProductEntity]) -> list[IDictionaryItemResponseModel]:
        ...
