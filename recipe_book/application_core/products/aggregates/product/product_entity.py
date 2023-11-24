from dataclasses import dataclass
from uuid import UUID

from ...interfaces.product_entity import IProductEntity


@dataclass
class ProductEntity(IProductEntity):
    uuid: UUID
    name: IProductEntity.name
    description: IProductEntity.description
    image_url: IProductEntity.image_url
