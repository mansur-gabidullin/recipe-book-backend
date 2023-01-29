from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .users import Users
from .groups import Groups


class UsersGroups(Base):
    __tablename__ = 'users_groups'

    id: Mapped[int] = mapped_column('id', primary_key=True)
    user_id = mapped_column('user_id', ForeignKey(Users.id), nullable=False)
    group_id = mapped_column('group_id', ForeignKey(Groups.id), nullable=False)
