from sqlalchemy import Column, Integer, Text

from .base import Base


class Roles(Base):
    __tablename__ = 'roles'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', Text, unique=True)
