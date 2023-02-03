from pydantic import BaseModel

from .ingredient import IngredientEntity


class InstructionStepEntity(BaseModel):
    title: str
    description: str
    ingredients: list[IngredientEntity]
