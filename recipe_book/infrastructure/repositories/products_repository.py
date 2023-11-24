from uuid import UUID

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.products.interfaces.products_repository import IProductsRepository

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
