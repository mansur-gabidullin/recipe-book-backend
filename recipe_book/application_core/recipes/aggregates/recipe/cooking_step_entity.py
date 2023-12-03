from dataclasses import dataclass

from ...interfaces.cooking_step_entity import ICookingStepEntity


@dataclass
class CookingStepEntity(ICookingStepEntity):
    description: str
    image_url: str = None
