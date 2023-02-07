from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base
from .users import Users


class Profiles(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    user_id = mapped_column("user_id", ForeignKey(Users.id), nullable=False)
    email: Mapped[str] = mapped_column("email", String(255))
    verified_email: Mapped[str] = mapped_column("verified_email", String(255))
    name: Mapped[str] = mapped_column("name", String(255), unique=True)
    surname: Mapped[str] = mapped_column("surname", String(255))
    patronymic: Mapped[str] = mapped_column("patronymic", String(255))
