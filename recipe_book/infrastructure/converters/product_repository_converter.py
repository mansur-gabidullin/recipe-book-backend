from ..helpers import scalar_as_dict
from ..beans.product_record import ProductRecord
from ..interfaces.product_repository_converter import IProductRepositoryConverter


class ProductRepositoryConverter(IProductRepositoryConverter):
    def from_query_results(self, results):
        products = []

        for item in results.mappings():
            products.append(ProductRecord(**scalar_as_dict(item.Products)))

        return products
