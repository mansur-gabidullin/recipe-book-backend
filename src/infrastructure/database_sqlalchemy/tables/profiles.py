from sqlalchemy import Column, Integer, Text

from .base import Base


class Profiles(Base):
    __tablename__ = 'profiles'

    id = Column('id', Integer, primary_key=True)
    email = Column('email', Text)
    verified_email = Column('verified_email', Text)
    name = Column('name', Text)
    surname = Column('surname', Text)
    patronymic = Column('patronymic', Text)
