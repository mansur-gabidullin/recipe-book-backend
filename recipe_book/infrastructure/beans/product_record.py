from dataclasses import dataclass
from uuid import UUID

from application_core.products.interfaces.product_record import IProductRecord


@dataclass
class ProductRecord(IProductRecord):
    uuid: UUID
    name: str
    description: str = None
    image_url: str = None
    is_removed: bool = False
