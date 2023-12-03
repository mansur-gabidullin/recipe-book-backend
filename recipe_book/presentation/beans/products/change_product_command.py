from dataclasses import dataclass

from application_core.products.interfaces.change_product_command import IChangeProductCommand


@dataclass
class ChangeProductCommand(IChangeProductCommand):
    name: str
    description: str = None
    image_url: str = None
