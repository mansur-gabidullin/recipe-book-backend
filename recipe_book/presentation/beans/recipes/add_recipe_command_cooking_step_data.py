from dataclasses import dataclass

from application_core.recipes.interfaces.add_recipe_command_cooking_step_data import IAddRecipeCommandCookingStepData

from .add_recipe_command_ingredient_data import AddRecipeCommandIngredientData


@dataclass
class AddRecipeCommandCookingStepData(IAddRecipeCommandCookingStepData):
    description: str
    image_url: str | None
    ingredients: list[AddRecipeCommandIngredientData]
