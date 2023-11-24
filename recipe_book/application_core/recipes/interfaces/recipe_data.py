from typing import runtime_checkable, Protocol

from .cooking_step_data import ICookingStepData


@runtime_checkable
class IRecipeData(Protocol):
    title: str
    description: str
    number_of_servings: int
    cooking_steps: list[ICookingStepData]
    image_url: str | None
    author: str | None
