from sqlalchemy import Column, Integer, ForeignKey

from .base import Base
from .groups import Groups
from .users import Users


class UsersGroups(Base):
    __tablename__ = 'users_groups'

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey(Users.id), nullable=False)
    group_id = Column('group_id', Integer, ForeignKey(Groups.id), nullable=False)
