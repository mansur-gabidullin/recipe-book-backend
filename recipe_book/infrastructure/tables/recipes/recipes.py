from uuid import uuid4

from sqlalchemy import Uuid, String, Integer
from sqlalchemy.orm import mapped_column, Mapped

from constants import (
    RECIPE_TITLE_MAX_LENGTH,
    RECIPE_DESCRIPTION_MAX_LENGTH,
    RECIPE_AUTHOR_MAX_LENGTH,
    RECIPE_IMAGE_URL_MAX_LENGTH,
)

from ..base import Base


class Recipes(Base):
    __tablename__ = "recipes"

    uuid = mapped_column("uuid", Uuid(as_uuid=True), primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column("title", String(RECIPE_TITLE_MAX_LENGTH), unique=True)
    description: Mapped[str] = mapped_column("description", String(RECIPE_DESCRIPTION_MAX_LENGTH))
    number_of_servings: Mapped[str] = mapped_column("number_of_servings", Integer)
    image_url: Mapped[str | None] = mapped_column("image_url", String(RECIPE_IMAGE_URL_MAX_LENGTH), nullable=True)
    author: Mapped[str | None] = mapped_column("author", String(RECIPE_AUTHOR_MAX_LENGTH), nullable=True)
