from sqlalchemy import Column, Integer, Text

from .base import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    login = Column('login', Text, unique=True, nullable=False)
    password_solt = Column('password_solt', Text, nullable=False)
    password_hash = Column('password_hash', Text, nullable=False)
