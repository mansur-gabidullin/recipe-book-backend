from beans.dtos.user import UserDTO
from beans.queries.users_list import UsersListQuery
from infrastructure.database_sqlalchemy.tables.users import Users
from ports.secondary import IDatabaseSession


class UsersRepository:
    def __init__(self, session: IDatabaseSession):
        self._session = session

    def get_users_list(self, query: UsersListQuery) -> list[UserDTO]:
        print(query)
        self._session.query(Users)
        return []
