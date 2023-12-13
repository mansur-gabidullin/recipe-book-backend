from uuid import UUID

from ..interfaces.add_product_command import IAddProductCommand
from ..interfaces.change_product_command import IChangeProductCommand
from ..interfaces.product_entity import IProductEntity
from ..interfaces.product_query import IProductQuery
from ..interfaces.products_query import IProductsQuery
from ..interfaces.products_service_converter import IProductsServiceConverter
from ..interfaces.products_repository import IProductsRepository
from ..interfaces.products_service import IProductsService
from ..interfaces.remove_product_command import IRemoveProductCommand


class ProductsService(IProductsService):
    def __init__(self, repository: IProductsRepository, converter: IProductsServiceConverter):
        self._repository = repository
        self._converter = converter

    async def get_product(self, query: IProductQuery) -> IProductEntity | None:
        record = await self._repository.get_product(query)
        return self._converter.from_record(record) if record else None

    async def get_products(self, query: IProductsQuery) -> list[IProductEntity]:
        records = await self._repository.get_products(query)
        return self._converter.from_records(records)

    async def add_product(self, command: IAddProductCommand) -> UUID:
        add_product_data = self._converter.to_product_data(command)
        return await self._repository.add_product(add_product_data)

    async def update_product(self, uuid: UUID, command: IChangeProductCommand) -> IProductEntity:
        data = self._converter.to_product_data(command)
        return self._converter.from_record(await self._repository.update_product(uuid, data))

    async def delete_product(self, command: IRemoveProductCommand) -> None:
        return await self._repository.delete_product(command)
