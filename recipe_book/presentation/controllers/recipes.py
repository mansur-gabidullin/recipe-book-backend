from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from application_core.recipes.interfaces.add_recipe_command import IAddRecipeCommand
from application_core.recipes.interfaces.recipes_query import IRecipesQuery
from application_core.recipes.interfaces.recipes_service import IRecipesService

from dependencies import (
    create_recipes_query,
    create_recipes_response_converter,
    create_recipes_service,
    create_add_recipe_command,
)

from ..interfaces.recipes.recipe_converter import IRecipeResponseConverter
from ..interfaces.recipes.new_recipe_response_model import INewRecipeResponseModel
from ..interfaces.recipes.recipe_response_model import IRecipeResponseModel

from ..beans.recipes.new_recipe_response_model import NewRecipeResponseModel
from ..beans.recipes.recipe_response_model import RecipeResponseModel

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("/", response_model=list[RecipeResponseModel])
async def get_recipes(
    recipes_query: IRecipesQuery = Depends(create_recipes_query),
    recipes_converter: IRecipeResponseConverter = Depends(create_recipes_response_converter),
    recipes_service: IRecipesService = Depends(create_recipes_service),
) -> list[IRecipeResponseModel]:
    recipes = await recipes_service.get_recipes(recipes_query)
    return recipes_converter.from_recipes(recipes)


@router.post("/", response_model=NewRecipeResponseModel)
async def add_recipe(
    add_recipe_command: IAddRecipeCommand = Depends(create_add_recipe_command),
    recipes_converter: IRecipeResponseConverter = Depends(create_recipes_response_converter),
    recipes_service: IRecipesService = Depends(create_recipes_service),
) -> INewRecipeResponseModel:
    try:
        recipe = await recipes_service.add_recipe(add_recipe_command)
    # todo: use custom error
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Incorrect data")
    return recipes_converter.from_new_recipe(recipe)
