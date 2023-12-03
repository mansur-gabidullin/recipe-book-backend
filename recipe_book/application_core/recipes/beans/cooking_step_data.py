from dataclasses import dataclass

from ..interfaces.cooking_step_data import ICookingStepData
from .ingredient_data import IngredientData


@dataclass
class CookingStepData(ICookingStepData):
    description: str
    ingredients: list[IngredientData]
    image_url: str = None
