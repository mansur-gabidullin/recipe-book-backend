from dataclasses import dataclass

from application_core.users.interfaces.users_query import IUsersQuery


@dataclass
class UsersQuery(IUsersQuery):
    login: str | None
    limit: int | None
