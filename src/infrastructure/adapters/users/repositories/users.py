from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.bounded_contexts.users.beans.dtos.user import UserDTO
from application_core.bounded_contexts.users.beans.queries.users import UsersQuery

from ....database_sqlalchemy.helpers import scalar_as_dict
from ....database_sqlalchemy.tables.users.profiles import Profiles
from ....database_sqlalchemy.tables.users.users import Users


class UsersRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_users(self, query: UsersQuery) -> list[UserDTO]:
        print(f'query = {query}')
        try:
            statement = select(Users, Profiles).join_from(Users, Profiles, isouter=True)
            result = await self._session.execute(statement)
            return [UserDTO(**scalar_as_dict(item)) for item in result.scalars()]
        except Exception as e:
            print(e)
            return []
