from typing import runtime_checkable, Protocol

from .add_recipe_command import IAddRecipeCommand
from .recipe_data import IRecipeData


@runtime_checkable
class IRecipesServiceConverter(Protocol):
    def to_recipe_data(self, data: IAddRecipeCommand) -> IRecipeData:
        ...
