from uuid import uuid4

from sqlalchemy import Uuid, ForeignKey, Boolean
from sqlalchemy.orm import mapped_column, Mapped

from application_core.recipes.interfaces.ingredient_quantity import IIngredientQuantity
from application_core.recipes.interfaces.ingredient_unit import IIngredientUnit

from ..base import Base
from ..products.products import Products
from .cooking_steps import CookingSteps


class Ingredients(Base):
    __tablename__ = "ingredients"

    uuid = mapped_column("uuid", Uuid(as_uuid=True), primary_key=True, default=uuid4)
    cooking_step_uuid = mapped_column("cooking_step_uuid", ForeignKey(CookingSteps.uuid))
    product_uuid = mapped_column("product_uuid", ForeignKey(Products.uuid))
    quantity: Mapped[IIngredientQuantity] = mapped_column("quantity")
    unit: Mapped[IIngredientUnit] = mapped_column("unit")
    is_removed: Mapped[bool] = mapped_column("is_removed", Boolean, default=False)
