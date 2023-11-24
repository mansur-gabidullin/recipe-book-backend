from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from application_core.products.interfaces.products_query import IProductsQuery
from application_core.products.interfaces.products_service import IProductsService
from application_core.products.interfaces.add_product_command import IAddProductCommand

from dependencies import (
    create_products_query,
    create_products_response_converter,
    create_products_service,
    create_add_product_command,
)

from ..interfaces.products.product_converter import IProductResponseConverter
from ..interfaces.products.new_product_response_model import INewProductResponseModel
from ..interfaces.products.product_response_model import IProductResponseModel
from ..beans.products.new_product_response_model import NewProductResponseModel
from ..beans.products.product_response_model import ProductResponseModel

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=list[ProductResponseModel])
async def get_products(
    products_query: IProductsQuery = Depends(create_products_query),
    products_converter: IProductResponseConverter = Depends(create_products_response_converter),
    products_service: IProductsService = Depends(create_products_service),
) -> list[IProductResponseModel]:
    products = await products_service.get_products(products_query)
    return products_converter.from_products(products)


@router.post("/", response_model=NewProductResponseModel)
async def add_product(
    add_product_command: IAddProductCommand = Depends(create_add_product_command),
    products_converter: IProductResponseConverter = Depends(create_products_response_converter),
    products_service: IProductsService = Depends(create_products_service),
) -> INewProductResponseModel:
    try:
        product = await products_service.add_product(add_product_command)
    # todo: use custom error
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Incorrect data")
    return products_converter.from_new_product(product)
