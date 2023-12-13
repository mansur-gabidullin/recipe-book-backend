from uuid import UUID

from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException
from starlette.responses import Response
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from dependencies import (
    create_products_query,
    create_products_response_converter,
    create_products_service,
    create_add_product_command,
    create_product_query,
    create_change_product_command,
    create_remove_product_command,
)

from application_core.products.interfaces.product_query import IProductQuery
from application_core.products.interfaces.products_query import IProductsQuery
from application_core.products.interfaces.products_service import IProductsService
from application_core.products.interfaces.add_product_command import IAddProductCommand
from application_core.products.interfaces.change_product_command import IChangeProductCommand
from application_core.products.interfaces.remove_product_command import IRemoveProductCommand

from ..interfaces.products.product_converter import IProductResponseConverter
from ..interfaces.products.new_product_response_model import INewProductResponseModel
from ..interfaces.products.product_response_model import IProductResponseModel

from ..beans.products.new_product_response_model import NewProductResponseModel
from ..beans.products.product_response_model import ProductResponseModel

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=list[ProductResponseModel])
async def get_products(
    query: IProductsQuery = Depends(create_products_query),
    converter: IProductResponseConverter = Depends(create_products_response_converter),
    service: IProductsService = Depends(create_products_service),
) -> list[IProductResponseModel]:
    products = await service.get_products(query)
    return converter.from_entities(products)


@router.post("/", response_model=NewProductResponseModel)
async def add_product(
    command: IAddProductCommand = Depends(create_add_product_command),
    converter: IProductResponseConverter = Depends(create_products_response_converter),
    service: IProductsService = Depends(create_products_service),
) -> INewProductResponseModel:
    try:
        product = await service.add_product(command)
    # todo: use custom error
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Incorrect data")
    return converter.from_new_product(product)


@router.get("/{uuid}", response_model=ProductResponseModel | None)
async def get_product(
    query: IProductQuery = Depends(create_product_query),
    converter: IProductResponseConverter = Depends(create_products_response_converter),
    service: IProductsService = Depends(create_products_service),
) -> IProductResponseModel | None:
    product = await service.get_product(query)
    return converter.from_entity(product) if product else None


@router.put("/{uuid}", response_model=ProductResponseModel)
async def update_product(
    uuid: UUID,
    command: IChangeProductCommand = Depends(create_change_product_command),
    converter: IProductResponseConverter = Depends(create_products_response_converter),
    service: IProductsService = Depends(create_products_service),
) -> INewProductResponseModel:
    try:
        product = await service.update_product(uuid, command)
    # todo: use custom error
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Incorrect data")
    return converter.from_entity(product)


@router.delete("/{uuid}", status_code=HTTP_204_NO_CONTENT, response_class=Response)
async def delete_product(
    command: IRemoveProductCommand = Depends(create_remove_product_command),
    service: IProductsService = Depends(create_products_service),
) -> None:
    return await service.delete_product(command)
