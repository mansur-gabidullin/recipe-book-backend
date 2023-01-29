from sqlalchemy import select

from application_core.bounded_contexts.users.beans.dtos.user import UserDTO
from application_core.bounded_contexts.users.beans.queries.users_list import UsersListQuery
from application_core.bounded_contexts.users.ports.secondary import IDatabaseSession
from infrastructure.database_sqlalchemy.helpers import scalar_as_dict
from infrastructure.database_sqlalchemy.tables.profiles import Profiles
from infrastructure.database_sqlalchemy.tables.users import Users


class UsersRepository:
    def __init__(self, session: IDatabaseSession):
        self._session = session

    async def get_users_list(self, query: UsersListQuery) -> list[UserDTO]:
        print(f'query = {query}')
        try:
            statement = select(Users, Profiles).join_from(Users, Profiles, isouter=True)
            result = await self._session.execute(statement)
            return [UserDTO(**scalar_as_dict(item)) for item in result.scalars()]
        except Exception as e:
            print(e)
            return []
