from dataclasses import dataclass

from ..interfaces.cooking_step_data import ICookingStepData
from ..interfaces.recipe_data import IRecipeData


@dataclass
class RecipeData(IRecipeData):
    title: str
    description: str
    number_of_servings: int
    cooking_steps: list[ICookingStepData]
    image_url: str | None
    author: str | None
