from dataclasses import dataclass

from ..interfaces.product_data import IProductData


@dataclass
class ProductData(IProductData):
    name: str
    description: str | None
    image_url: str | None
