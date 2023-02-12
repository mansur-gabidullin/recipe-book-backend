from pydantic import BaseModel


class IngredientEntity(BaseModel):
    name: str
    amount: str
