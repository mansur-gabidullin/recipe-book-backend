from sqlalchemy import Column, Integer, Text

from .base import Base


class Permissions(Base):
    __tablename__ = 'permissions'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', Text, unique=True)
