from uuid import uuid4

from sqlalchemy import ForeignKey, Uuid, Boolean
from sqlalchemy.orm import mapped_column, Mapped

from ..base import Base
from .roles import Roles
from .permissions import Permissions


class RolesPermissions(Base):
    __tablename__ = "roles_permissions"

    uuid = mapped_column("uuid", Uuid(as_uuid=True), primary_key=True, default=uuid4)
    role_uuid = mapped_column("role_uuid", ForeignKey(Roles.uuid))
    permission_uuid = mapped_column("permission_uuid", ForeignKey(Permissions.uuid))
    is_removed: Mapped[bool] = mapped_column("is_removed", Boolean, default=False)
