from dataclasses import dataclass
from uuid import UUID

from ...interfaces.recipe_entity import IRecipeEntity
from .cooking_step_entity import CookingStepEntity


@dataclass
class RecipeEntity(IRecipeEntity):
    uuid: UUID
    title: str
    description: str
    number_of_servings: int
    cooking_steps: list[CookingStepEntity]
    image_url: str = None
    author: str = None
