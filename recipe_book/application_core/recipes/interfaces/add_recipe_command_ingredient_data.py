from typing import Protocol, runtime_checkable
from uuid import UUID

from .ingredient_quantity import IIngredientQuantity
from .ingredient_unit import IIngredientUnit


@runtime_checkable
class IAddRecipeCommandIngredientData(Protocol):
    product_uuid: UUID
    quantity: IIngredientQuantity
    unit: IIngredientUnit
