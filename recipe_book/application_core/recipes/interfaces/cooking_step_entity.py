from typing import Protocol, runtime_checkable

from .ingredient_entity import IIngredientEntity


@runtime_checkable
class ICookingStepEntity(Protocol):
    description: str
    image_url: str | None
    ingredients: list[IIngredientEntity]
