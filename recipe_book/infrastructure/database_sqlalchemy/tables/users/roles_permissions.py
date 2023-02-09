from uuid import uuid4

from sqlalchemy import ForeignKey, Uuid
from sqlalchemy.orm import mapped_column

from ..base import Base
from .roles import Roles
from .permissions import Permissions


class RolesPermissions(Base):
    __tablename__ = "roles_permissions"

    uuid = mapped_column("uuid", Uuid(as_uuid=True), primary_key=True, default=uuid4)
    role_id = mapped_column("role_id", ForeignKey(Roles.uuid), nullable=False)
    permission_id = mapped_column("permission_id", ForeignKey(Permissions.uuid), nullable=False)
