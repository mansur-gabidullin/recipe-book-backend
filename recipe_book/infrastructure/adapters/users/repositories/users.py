from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.bounded_contexts.users.beans.user_po import UserPO
from application_core.bounded_contexts.users.beans.users_query_dto import UsersQueryDTO
from application_core.bounded_contexts.users.entities.user import UserEntity

from ....database_sqlalchemy.helpers import scalar_as_dict
from ....database_sqlalchemy.tables.users.profiles import Profiles
from ....database_sqlalchemy.tables.users.users import Users


class UsersRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_users(self, query: UsersQueryDTO) -> list[UserEntity]:
        print(f"query = {query}")
        try:
            statement = select(Users, Profiles).join_from(Users, Profiles, isouter=True)
            result = await self._session.execute(statement)
            return [UserEntity(**scalar_as_dict(item)) for item in result.scalars()]
        except Exception as e:
            print(e)
            raise e

    async def add_user(self, user: UserPO) -> int:
        try:
            values = {
                Users.login.key: user.login,
                Users.password_solt.key: user.password_solt,
                Users.password_hash.key: user.password_hash,
            }
            statement = insert(Users).values(values).returning(Users.id)
            result = await self._session.execute(statement)
            (created_id,) = result.one()
            return created_id
        except Exception as e:
            print(e)
            raise e
