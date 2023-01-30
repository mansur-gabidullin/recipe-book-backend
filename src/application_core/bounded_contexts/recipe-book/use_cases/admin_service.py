from ..beans.recipe_dto import RecipeDTO
from ..beans.recipes_query_dto import RecipesQueryDTO
from ..ports.secondary import IRecipesRepository


class RecipeBookAdminUseCase:
    def __init__(self, repository: IRecipesRepository):
        self._repository = repository

    async def fetch_recipes(self, query: RecipesQueryDTO) -> list[RecipeDTO]:
        return await self._repository.get_recipes(query)
