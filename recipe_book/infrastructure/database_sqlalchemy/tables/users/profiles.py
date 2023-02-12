from uuid import uuid4

from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from application_core.bounded_contexts.users.constants import (
    EMAIL_MAX_LENGTH,
    USER_NAME_MAX_LENGTH,
    USER_NICKNAME_MAX_LENGTH,
    USER_SURNAME_MAX_LENGTH,
    USER_PATRONYMIC_MAX_LENGTH,
)
from ..base import Base
from .users import Users


class Profiles(Base):
    __tablename__ = "profiles"

    uuid = mapped_column("uuid", Uuid(as_uuid=True), primary_key=True, default=uuid4)
    user_uuid = mapped_column("user_uuid", ForeignKey(Users.uuid))
    email: Mapped[str] = mapped_column("email", String(EMAIL_MAX_LENGTH))
    verified_email: Mapped[str] = mapped_column("verified_email", String(EMAIL_MAX_LENGTH), nullable=True)
    name: Mapped[str] = mapped_column("name", String(USER_NAME_MAX_LENGTH), nullable=True)
    nickname: Mapped[str] = mapped_column("nickname", String(USER_NICKNAME_MAX_LENGTH), nullable=True)
    surname: Mapped[str] = mapped_column("surname", String(USER_SURNAME_MAX_LENGTH), nullable=True)
    patronymic: Mapped[str] = mapped_column("patronymic", String(USER_PATRONYMIC_MAX_LENGTH), nullable=True)
