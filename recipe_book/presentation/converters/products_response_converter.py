from application_core.products.interfaces.product_entity import IProductEntity
from ..beans.products.product_response_model import ProductResponseModel

from ..interfaces.products.product_converter import IProductResponseConverter
from ..interfaces.products.product_response_model import IProductResponseModel
from ..beans.products.new_product_response_model import NewProductResponseModel


class ProductResponseConverter(IProductResponseConverter):
    def from_entity(self, product: IProductEntity) -> IProductResponseModel:
        return ProductResponseModel(
            uuid=product.uuid,
            name=product.name,
            description=product.description,
            image_url=product.image_url,
        )

    def from_entities(self, products: list[IProductEntity]) -> list[IProductResponseModel]:
        return [self.from_entity(product) for product in products]

    def from_new_product(self, uuid):
        return NewProductResponseModel(uuid=uuid)
