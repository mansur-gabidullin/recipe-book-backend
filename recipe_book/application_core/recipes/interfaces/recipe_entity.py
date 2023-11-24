from typing import Protocol, runtime_checkable
from uuid import UUID

from ..interfaces.cooking_step_entity import ICookingStepEntity


@runtime_checkable
class IRecipeEntity(Protocol):
    uuid: UUID
    title: str
    description: str
    number_of_servings: int
    cooking_steps: list[ICookingStepEntity]
    image_url: str | None
    author: str | None
