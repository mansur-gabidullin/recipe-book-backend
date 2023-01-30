from typing import Protocol

from ..beans.recipes_query_dto import RecipesQueryDTO
from ..beans.recipe_dto import RecipeDTO


class IRecipesRepository(Protocol):
    async def get_recipes(self, query: RecipesQueryDTO) -> list[RecipeDTO]:
        ...
