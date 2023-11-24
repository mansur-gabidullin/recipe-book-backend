from typing import Protocol, runtime_checkable

from .ingredient_data import IIngredientData


@runtime_checkable
class ICookingStepData(Protocol):
    description: str
    image_url: str | None
    ingredients: list[IIngredientData]
