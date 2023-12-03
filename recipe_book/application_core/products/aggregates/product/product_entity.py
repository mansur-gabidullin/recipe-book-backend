from dataclasses import dataclass
from uuid import UUID

from ...interfaces.product_entity import IProductEntity


@dataclass
class ProductEntity(IProductEntity):
    uuid: UUID
    name: str
    description: str = None
    image_url: str = None
    is_removed: bool = False
