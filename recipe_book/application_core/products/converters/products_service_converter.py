from ..interfaces.product_data import IProductData
from ..interfaces.products_service_converter import IProductsServiceConverter
from ..beans.product_data import ProductData


class ProductsServiceConverter(IProductsServiceConverter):
    def to_product_data(self, data) -> IProductData:
        return ProductData(
            name=data.name,
            description=data.description,
            image_url=data.image_url,
        )
