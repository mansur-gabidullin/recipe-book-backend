from uuid import UUID

from ..interfaces.add_product_command import IAddProductCommand
from ..interfaces.products_service_converter import IProductsServiceConverter
from ..interfaces.products_repository import IProductsRepository
from ..interfaces.products_service import IProductsService


class ProductsService(IProductsService):
    def __init__(self, repository: IProductsRepository, converter: IProductsServiceConverter):
        self._repository = repository
        self._converter = converter

    async def add_product(self, add_product_command: IAddProductCommand) -> UUID:
        add_product_data = self._converter.to_product_data(add_product_command)
        return await self._repository.add_product(add_product_data)
