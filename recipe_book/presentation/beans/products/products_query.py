from dataclasses import dataclass

from application_core.products.interfaces.products_query import IProductsQuery


@dataclass
class ProductsQuery(IProductsQuery):
    limit: int | None
    is_removed: bool = False
