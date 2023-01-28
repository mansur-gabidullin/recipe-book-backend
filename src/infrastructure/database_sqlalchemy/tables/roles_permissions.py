from sqlalchemy import Column, Integer, ForeignKey

from .base import Base
from .permissions import Permissions
from .roles import Roles


class RolesPermissions(Base):
    __tablename__ = 'roles_permissions'

    id = Column('id', Integer, primary_key=True)
    role_id = Column('role_id', Integer, ForeignKey(Roles.id), nullable=False)
    permission_id = Column('permission_id', Integer, ForeignKey(Permissions.id), nullable=False)
