from typing import Protocol

from sqlalchemy.orm import Session

from beans.dtos.user import UserDTO
from beans.queries.users_list import UsersListQuery

IDatabaseSession = Session


class IUsersRepository(Protocol):
    def get_users_list(self, query: UsersListQuery) -> list[UserDTO]:
        ...
