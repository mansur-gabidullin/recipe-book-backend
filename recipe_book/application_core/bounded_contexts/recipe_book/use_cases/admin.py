from dataclasses import asdict

from ..beans.recipe_dto import RecipeDTO
from ..beans.recipes_query_dto import RecipesQueryDTO
from ..ports.secondary import IRecipesRepository


class RecipeBookAdminUseCase:
    def __init__(self, repository: IRecipesRepository):
        self._repository = repository

    async def handle_recipes_query(self, query: RecipesQueryDTO) -> list[RecipeDTO]:
        return [RecipeDTO(**asdict(recipe)) for recipe in await self._repository.get_recipes(query)]
