from pydantic import BaseModel

from .instruction_step import InstructionStepEntity


class RecipeEntity(BaseModel):
    title: str
    description: str
    instruction_steps: list[InstructionStepEntity]
