from typing import runtime_checkable, Protocol
from uuid import UUID

from .new_recipe_response_model import INewRecipeResponseModel
from .recipe_response_model import IRecipeResponseModel


@runtime_checkable
class IRecipeResponseConverter(Protocol):
    def from_recipes(self, recipes) -> list[IRecipeResponseModel]:
        ...

    def from_new_recipe(self, uuid: UUID) -> INewRecipeResponseModel:
        ...
