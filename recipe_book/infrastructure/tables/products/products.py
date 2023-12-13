from uuid import uuid4

from sqlalchemy import Uuid, String
from sqlalchemy.orm import mapped_column, Mapped

from constants import RECIPE_DESCRIPTION_MAX_LENGTH, RECIPE_IMAGE_URL_MAX_LENGTH, RECIPE_TITLE_MAX_LENGTH

from ..base import Base


class Products(Base):
    __tablename__ = "products"

    uuid = mapped_column("uuid", Uuid(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column("name", String(RECIPE_TITLE_MAX_LENGTH), unique=True)
    description: Mapped[str | None] = mapped_column("description", String(RECIPE_DESCRIPTION_MAX_LENGTH))
    image_url: Mapped[str | None] = mapped_column("image_url", String(RECIPE_IMAGE_URL_MAX_LENGTH), nullable=True)
