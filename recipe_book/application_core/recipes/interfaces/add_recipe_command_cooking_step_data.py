from typing import Protocol, runtime_checkable

from .add_recipe_command_ingredient_data import IAddRecipeCommandIngredientData


@runtime_checkable
class IAddRecipeCommandCookingStepData(Protocol):
    description: str
    image_url: str | None
    ingredients: list[IAddRecipeCommandIngredientData]
