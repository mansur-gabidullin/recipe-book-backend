from dataclasses import dataclass
from uuid import UUID

from application_core.products.interfaces.remove_product_command import IRemoveProductCommand


@dataclass
class RemoveProductCommand(IRemoveProductCommand):
    uuid: UUID
