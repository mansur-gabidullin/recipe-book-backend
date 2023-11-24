from ...interfaces.cooking_step_entity import ICookingStepEntity


class CookingStepEntity(ICookingStepEntity):
    description: str
    image_url: str | None
