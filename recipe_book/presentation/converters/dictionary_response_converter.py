from application_core.products.interfaces.product_entity import IProductEntity

from ..interfaces.dictionary.dictionary_converter import IDictionaryResponseConverter
from ..interfaces.dictionary.dictionary_item_response_model import IDictionaryItemResponseModel
from ..beans.dictionary.dictionary_item_response_model import DictionaryItemResponseModel


class DictionaryResponseConverter(IDictionaryResponseConverter):
    def from_entity(self, product: IProductEntity) -> IDictionaryItemResponseModel:
        return DictionaryItemResponseModel(code=str(product.uuid), title=product.name)

    def from_entities(self, products: list[IProductEntity]) -> list[IDictionaryItemResponseModel]:
        return [self.from_entity(product) for product in products]
