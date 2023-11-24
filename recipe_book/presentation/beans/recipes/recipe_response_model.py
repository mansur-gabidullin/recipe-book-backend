from dataclasses import dataclass
from uuid import UUID

from ...interfaces.recipes.recipe_response_model import IRecipeResponseModel


@dataclass
class RecipeResponseModel(IRecipeResponseModel):
    uuid: UUID
