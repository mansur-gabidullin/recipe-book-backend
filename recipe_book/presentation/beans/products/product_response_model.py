from dataclasses import dataclass
from uuid import UUID

from ...interfaces.products.product_response_model import IProductResponseModel


@dataclass
class ProductResponseModel(IProductResponseModel):
    uuid: UUID
    name: str
    description: str = None
    image_url: str = None
