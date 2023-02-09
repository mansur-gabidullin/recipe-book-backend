from uuid import uuid4

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from application_core.bounded_contexts.users.constants import PERMISSION_NAME_MAX_LENGTH
from ..base import Base


class Permissions(Base):
    __tablename__ = "permissions"

    uuid = mapped_column("uuid", Uuid(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column("name", String(PERMISSION_NAME_MAX_LENGTH), unique=True)
