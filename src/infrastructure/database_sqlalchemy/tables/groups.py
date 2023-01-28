from sqlalchemy import Column, Integer, Text

from .base import Base


class Groups(Base):
    __tablename__ = 'groups'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', Text, unique=True)
