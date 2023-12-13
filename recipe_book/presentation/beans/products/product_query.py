from dataclasses import dataclass
from uuid import UUID

from application_core.products.interfaces.product_query import IProductQuery


@dataclass
class ProductQuery(IProductQuery):
    uuid: UUID
