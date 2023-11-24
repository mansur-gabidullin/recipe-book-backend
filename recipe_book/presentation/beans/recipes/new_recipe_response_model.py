from dataclasses import dataclass
from uuid import UUID

from ...interfaces.recipes.new_recipe_response_model import INewRecipeResponseModel


@dataclass
class NewRecipeResponseModel(INewRecipeResponseModel):
    uuid: UUID
