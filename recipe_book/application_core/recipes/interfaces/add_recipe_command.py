from typing import runtime_checkable, Protocol

from .add_recipe_command_cooking_step_data import IAddRecipeCommandCookingStepData


@runtime_checkable
class IAddRecipeCommand(Protocol):
    title: str
    description: str
    number_of_servings: int
    cooking_steps: list[IAddRecipeCommandCookingStepData]
    image_url: str | None
    author: str | None
