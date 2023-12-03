from uuid import uuid4

from sqlalchemy import String, Uuid, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from constants import ROLE_NAME_MAX_LENGTH
from ..base import Base


class Roles(Base):
    __tablename__ = "roles"

    uuid = mapped_column("uuid", Uuid(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column("name", String(ROLE_NAME_MAX_LENGTH), unique=True)
    is_removed: Mapped[bool] = mapped_column("is_removed", Boolean, default=False)
