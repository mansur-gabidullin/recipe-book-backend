from ..beans.products.new_product_response_model import NewProductResponseModel
from ..interfaces.products.product_converter import IProductResponseConverter


class ProductResponseConverter(IProductResponseConverter):
    def from_products(self, products):
        return []

    def from_new_product(self, uuid):
        return NewProductResponseModel(uuid=uuid)
