from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Permissions(Base):
    __tablename__ = 'permissions'

    id: Mapped[int] = mapped_column('id', primary_key=True)
    name: Mapped[str] = mapped_column('name', String(255), unique=True)
