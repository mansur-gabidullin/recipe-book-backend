from uuid import uuid4

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from application_core.users.constants import GROUP_NAME_MAX_LENGTH
from ..base import Base


class Groups(Base):
    __tablename__ = "groups"

    uuid = mapped_column("uuid", Uuid(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column("name", String(GROUP_NAME_MAX_LENGTH), unique=True)
