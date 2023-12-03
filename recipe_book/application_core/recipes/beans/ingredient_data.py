from dataclasses import dataclass
from uuid import UUID

from ..interfaces.ingredient_data import IIngredientData
from ..interfaces.ingredient_quantity import IIngredientQuantity
from ..interfaces.ingredient_unit import IIngredientUnit


@dataclass
class IngredientData(IIngredientData):
    product_uuid: UUID
    quantity: IIngredientQuantity
    unit: IIngredientUnit
