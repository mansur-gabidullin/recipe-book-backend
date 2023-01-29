from sqlalchemy import Text, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column('id', primary_key=True)
    login: Mapped[str] = mapped_column('login', String(255), unique=True, nullable=False)
    password_solt: Mapped[str] = mapped_column('password_solt', Text, nullable=False)
    password_hash: Mapped[str] = mapped_column('password_hash', Text, nullable=False)
