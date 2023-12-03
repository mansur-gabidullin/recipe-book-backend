from ..interfaces.product_data import IProductData
from ..interfaces.product_entity import IProductEntity
from ..interfaces.product_record import IProductRecord
from ..interfaces.products_service_converter import IProductsServiceConverter
from ..beans.product_data import ProductData
from ..aggregates.product.product_entity import ProductEntity


class ProductsServiceConverter(IProductsServiceConverter):
    def from_record(self, record: IProductRecord) -> IProductEntity:
        return ProductEntity(
            uuid=record.uuid,
            name=record.name,
            description=record.description,
            image_url=record.image_url,
            is_removed=record.is_removed,
        )

    def from_records(self, records: list[IProductRecord]) -> list[IProductEntity]:
        return [self.from_record(record) for record in records]

    def to_product_data(self, data) -> IProductData:
        return ProductData(
            name=data.name,
            description=data.description,
            image_url=data.image_url,
        )
