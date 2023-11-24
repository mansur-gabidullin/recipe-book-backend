from dataclasses import dataclass
from uuid import UUID

from application_core.recipes.interfaces.add_recipe_command_ingredient_data import IAddRecipeCommandIngredientData
from application_core.recipes.interfaces.ingredient_quantity import IIngredientQuantity
from application_core.recipes.interfaces.ingredient_unit import IIngredientUnit


@dataclass
class AddRecipeCommandIngredientData(IAddRecipeCommandIngredientData):
    product_uuid: UUID
    quantity: IIngredientQuantity
    unit: IIngredientUnit
