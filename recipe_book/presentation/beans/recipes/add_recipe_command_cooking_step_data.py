from dataclasses import dataclass
from typing import Annotated

from pydantic import StringConstraints

from constants import RECIPE_DESCRIPTION_MIN_LENGTH, RECIPE_DESCRIPTION_MAX_LENGTH, RECIPE_IMAGE_URL_MAX_LENGTH

from application_core.recipes.interfaces.add_recipe_command_cooking_step_data import IAddRecipeCommandCookingStepData

from .add_recipe_command_ingredient_data import AddRecipeCommandIngredientData


@dataclass
class AddRecipeCommandCookingStepData(IAddRecipeCommandCookingStepData):
    description: Annotated[
        str, StringConstraints(min_length=RECIPE_DESCRIPTION_MIN_LENGTH, max_length=RECIPE_DESCRIPTION_MAX_LENGTH)
    ]
    ingredients: list[AddRecipeCommandIngredientData]
    image_url: Annotated[str, StringConstraints(max_length=RECIPE_IMAGE_URL_MAX_LENGTH)] = None
