from dataclasses import dataclass
from uuid import UUID

from ...interfaces.ingredient_entity import IIngredientEntity


@dataclass
class IngredientEntity(IIngredientEntity):
    uuid: UUID
    name: str
