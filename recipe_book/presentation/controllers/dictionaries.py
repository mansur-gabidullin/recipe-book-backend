from fastapi import APIRouter, Depends

from dependencies import create_products_service, create_products_query, create_dictionary_response_converter

from application_core.products.interfaces.products_query import IProductsQuery
from application_core.products.interfaces.products_service import IProductsService

from ..interfaces.dictionary.dictionary_converter import IDictionaryResponseConverter
from ..interfaces.dictionary.dictionary_item_response_model import IDictionaryItemResponseModel
from ..beans.dictionary.dictionary_item_response_model import DictionaryItemResponseModel

router = APIRouter(prefix="/dictionary", tags=["dictionary"])


@router.get("/products", response_model=list[DictionaryItemResponseModel])
async def get_products_dictionary(
    query: IProductsQuery = Depends(create_products_query),
    converter: IDictionaryResponseConverter = Depends(create_dictionary_response_converter),
    products_service: IProductsService = Depends(create_products_service),
) -> list[IDictionaryItemResponseModel]:
    products = await products_service.get_products(query)
    return converter.from_entities(products)
