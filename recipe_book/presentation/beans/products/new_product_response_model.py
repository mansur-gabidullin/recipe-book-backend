from dataclasses import dataclass
from uuid import UUID

from ...interfaces.products.new_product_response_model import INewProductResponseModel


@dataclass
class NewProductResponseModel(INewProductResponseModel):
    uuid: UUID
