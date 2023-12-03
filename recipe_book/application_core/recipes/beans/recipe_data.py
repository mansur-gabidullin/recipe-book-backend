from dataclasses import dataclass

from ..interfaces.recipe_data import IRecipeData
from .cooking_step_data import CookingStepData


@dataclass
class RecipeData(IRecipeData):
    title: str
    description: str
    number_of_servings: int
    cooking_steps: list[CookingStepData]
    image_url: str = None
    author: str = None
