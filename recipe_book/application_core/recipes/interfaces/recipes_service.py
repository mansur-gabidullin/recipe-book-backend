from typing import runtime_checkable, Protocol
from uuid import UUID

from .add_recipe_command import IAddRecipeCommand
from .recipe_entity import IRecipeEntity
from .recipes_query import IRecipesQuery


@runtime_checkable
class IRecipesService(Protocol):
    async def get_recipes(self, recipes_query: IRecipesQuery) -> list[IRecipeEntity]:
        ...

    async def add_recipe(self, add_recipe_command: IAddRecipeCommand) -> UUID:
        ...
