from uuid import UUID

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.products.interfaces.product_data import IProductData
from application_core.products.interfaces.product_query import IProductQuery
from application_core.products.interfaces.product_record import IProductRecord
from application_core.products.interfaces.products_query import IProductsQuery
from application_core.products.interfaces.products_repository import IProductsRepository
from application_core.products.interfaces.remove_product_command import IRemoveProductCommand

from ..interfaces.product_repository_converter import IProductRepositoryConverter
from ..tables.products.products import Products


class ProductsRepository(IProductsRepository):
    def __init__(
        self,
        session: AsyncSession,
        converter: IProductRepositoryConverter,
    ):
        self._session = session
        self._converter = converter

    async def get_product(self, query: IProductQuery) -> IProductRecord | None:
        statement = (
            select(Products).where((Products.uuid == query.uuid) & (Products.is_removed == query.is_removed)).limit(1)
        )

        records = self._converter.from_query_results(await self._session.execute(statement))

        return records[0] if len(records) > 0 else None

    async def get_products(self, query: IProductsQuery) -> list[IProductRecord]:
        statement = select(Products).where(Products.is_removed == query.is_removed)

        if query.limit:
            statement = statement.limit(query.limit)

        return self._converter.from_query_results(await self._session.execute(statement))

    async def add_product(self, data) -> UUID:
        statement = (
            insert(Products)
            .values(
                {
                    Products.name.key: data.name,
                    Products.description.key: data.description,
                    Products.image_url.key: data.image_url,
                }
            )
            .returning(Products.uuid)
        )

        [product_uuid] = (await self._session.execute(statement)).one()

        return product_uuid

    async def update_product(self, uuid: UUID, data: IProductData) -> IProductRecord:
        statement = (
            update(Products)
            .where(Products.uuid == uuid)
            .values(
                {
                    Products.name.key: data.name,
                    Products.description.key: data.description,
                    Products.image_url.key: data.image_url,
                }
            )
            .returning(Products)
        )

        return self._converter.from_query_results(await self._session.execute(statement))[0]

    async def remove_product(self, command: IRemoveProductCommand) -> None:
        update_statement = update(Products).where(Products.uuid == command.uuid).values({Products.is_removed.key: True})

        await self._session.execute(update_statement)

    async def delete_product(self, command: IRemoveProductCommand) -> None:
        delete_statement = delete(Products).where(Products.uuid == command.uuid)
        await self._session.execute(delete_statement)
