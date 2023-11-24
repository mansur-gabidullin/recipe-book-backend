from uuid import uuid4

from sqlalchemy import Uuid, String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from constants import RECIPE_DESCRIPTION_MAX_LENGTH, RECIPE_IMAGE_URL_MAX_LENGTH

from ..base import Base
from .recipes import Recipes


class CookingSteps(Base):
    __tablename__ = "cooking_steps"

    uuid = mapped_column("uuid", Uuid(as_uuid=True), primary_key=True, default=uuid4)
    recipe_uuid = mapped_column("recipe_uuid", ForeignKey(Recipes.uuid))
    description: Mapped[str] = mapped_column("description", String(RECIPE_DESCRIPTION_MAX_LENGTH))
    image_url: Mapped[str | None] = mapped_column("image_url", String(RECIPE_IMAGE_URL_MAX_LENGTH), nullable=True)
