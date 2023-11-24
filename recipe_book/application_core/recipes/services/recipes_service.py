from uuid import UUID

from ..interfaces.recipe_entity import IRecipeEntity
from ..interfaces.recipes_service_converter import IRecipesServiceConverter
from ..interfaces.recipes_repository import IRecipesRepository
from ..interfaces.recipes_service import IRecipesService


class RecipesService(IRecipesService):
    def __init__(self, repository: IRecipesRepository, converter: IRecipesServiceConverter):
        self._repository = repository
        self._converter = converter

    async def get_recipes(self, recipes_query) -> list[IRecipeEntity]:
        return []

    async def add_recipe(self, add_recipe_command) -> UUID:
        add_recipe_data = self._converter.to_recipe_data(add_recipe_command)
        return await self._repository.add_recipe(add_recipe_data)
