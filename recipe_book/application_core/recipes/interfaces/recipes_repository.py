from typing import runtime_checkable, Protocol
from uuid import UUID

from .recipe_data import IRecipeData
from .recipe_entity import IRecipeEntity


@runtime_checkable
class IRecipesRepository(Protocol):
    async def get_recipes(self, data: IRecipeData) -> list[IRecipeEntity]:
        ...

    async def add_recipe(self, data: IRecipeData) -> UUID:
        ...
