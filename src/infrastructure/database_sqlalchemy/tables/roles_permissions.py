from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .roles import Roles
from .permissions import Permissions


class RolesPermissions(Base):
    __tablename__ = 'roles_permissions'

    id: Mapped[int] = mapped_column('id', primary_key=True)
    role_id = mapped_column('role_id', ForeignKey(Roles.id), nullable=False)
    permission_id = mapped_column('permission_id', ForeignKey(Permissions.id), nullable=False)
