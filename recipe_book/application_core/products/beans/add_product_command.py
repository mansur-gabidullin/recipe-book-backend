from dataclasses import dataclass

from ..interfaces.add_product_command import IAddProductCommand


@dataclass
class AddProductCommand(IAddProductCommand):
    name: str
    description: str = None
    image_url: str = None
