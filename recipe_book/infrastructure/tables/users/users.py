from uuid import uuid4

from sqlalchemy import Text, String, Uuid, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from application_core.users.constants import USER_LOGIN_MAX_LENGTH

from ..base import Base


class Users(Base):
    __tablename__ = "users"

    uuid = mapped_column("uuid", Uuid(as_uuid=True), primary_key=True, default=uuid4)
    login: Mapped[str] = mapped_column("login", String(USER_LOGIN_MAX_LENGTH), unique=True)
    password_hash: Mapped[str] = mapped_column("password_hash", Text)
    is_removed: Mapped[bool] = mapped_column("is_removed", Boolean, default=False)
    is_active: Mapped[bool] = mapped_column("is_active", Boolean, default=False)
