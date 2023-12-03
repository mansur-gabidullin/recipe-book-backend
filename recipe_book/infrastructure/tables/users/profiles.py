from uuid import uuid4

from sqlalchemy import ForeignKey, String, Uuid, CheckConstraint, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from constants import (
    USER_EMAIL_MAX_LENGTH,
    USER_NAME_MAX_LENGTH,
    USER_NICKNAME_MAX_LENGTH,
    USER_SURNAME_MAX_LENGTH,
    USER_PATRONYMIC_MAX_LENGTH,
    USER_PHONE_NUMBER_MAX_LENGTH,
)
from ..base import Base
from .users import Users


class Profiles(Base):
    __tablename__ = "profiles"

    uuid = mapped_column("uuid", Uuid(as_uuid=True), primary_key=True, default=uuid4)
    user_uuid = mapped_column("user_uuid", ForeignKey(Users.uuid))
    email: Mapped[str] = mapped_column("email", String(USER_EMAIL_MAX_LENGTH))
    phone_number: Mapped[str | None] = mapped_column(
        "phone_number", String(USER_PHONE_NUMBER_MAX_LENGTH), nullable=True
    )
    verified_email: Mapped[str | None] = mapped_column("verified_email", String(USER_EMAIL_MAX_LENGTH), nullable=True)
    verified_phone_number: Mapped[str | None] = mapped_column(
        "verified_phone_number", String(USER_PHONE_NUMBER_MAX_LENGTH), nullable=True
    )
    name: Mapped[str | None] = mapped_column("name", String(USER_NAME_MAX_LENGTH), nullable=True)
    nickname: Mapped[str | None] = mapped_column("nickname", String(USER_NICKNAME_MAX_LENGTH), nullable=True)
    surname: Mapped[str | None] = mapped_column("surname", String(USER_SURNAME_MAX_LENGTH), nullable=True)
    patronymic: Mapped[str | None] = mapped_column("patronymic", String(USER_PATRONYMIC_MAX_LENGTH), nullable=True)
    is_removed: Mapped[bool] = mapped_column("is_removed", Boolean, default=False)


CheckConstraint(Profiles.email.like("_%@_%.__%"), name=f"{Profiles.email.key}_is_email")
CheckConstraint(Profiles.verified_email.like("_%@_%.__%"), name=f"{Profiles.verified_email.key}_is_email")

CheckConstraint(Profiles.phone_number.regexp_match(r"^\+\d+$"), name=f"{Profiles.phone_number.key}_is_phone_number")
CheckConstraint(
    Profiles.verified_phone_number.regexp_match(r"^\+\d+$"),
    name=f"{Profiles.verified_phone_number.key}_is_phone_number",
)
