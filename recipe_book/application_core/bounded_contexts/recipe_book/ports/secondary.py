from typing import Protocol

from ..beans.recipes_query_dto import RecipesQueryDTO
from ..aggregates.recipe.root import RecipeEntity


class IRecipesRepository(Protocol):
    async def get_recipes(self, query: RecipesQueryDTO) -> list[RecipeEntity]:
        ...
