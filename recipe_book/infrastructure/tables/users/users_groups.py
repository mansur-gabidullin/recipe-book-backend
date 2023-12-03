from uuid import uuid4

from sqlalchemy import ForeignKey, Uuid, Boolean
from sqlalchemy.orm import mapped_column, Mapped

from ..base import Base
from .users import Users
from .groups import Groups


class UsersGroups(Base):
    __tablename__ = "users_groups"

    uuid = mapped_column("uuid", Uuid(as_uuid=True), primary_key=True, default=uuid4)
    user_uuid = mapped_column("user_uuid", ForeignKey(Users.uuid))
    group_uuid = mapped_column("group_uuid", ForeignKey(Groups.uuid))
    is_removed: Mapped[bool] = mapped_column("is_removed", Boolean, default=False)
