from uuid import UUID

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.bounded_contexts.users.beans.user_po import UserPO
from application_core.bounded_contexts.users.beans.queries.users_query_dto import UsersQueryDTO
from application_core.bounded_contexts.users.entities.user import UserEntity
from application_core.bounded_contexts.users.ports.secondary import IUsersRepository

from ....database_sqlalchemy.helpers import scalar_as_dict
from ....database_sqlalchemy.tables.users.profiles import Profiles
from ....database_sqlalchemy.tables.users.users import Users


class UsersRepository(IUsersRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_users(self, query: UsersQueryDTO) -> list[UserEntity]:
        print(f"query = {query}")
        statement = select(Users, Profiles).join_from(Users, Profiles, isouter=True)
        result = await self._session.execute(statement)
        return [UserEntity(**scalar_as_dict(item)) for item in result.scalars()]

    async def add_user(self, user: UserPO) -> UUID:
        statement = (
            insert(Users)
            .values(
                {
                    Users.login.key: user.login,
                    Users.password_hash.key: user.password_hash,
                }
            )
            .returning(Users.uuid)
        )

        (uuid,) = (await self._session.execute(statement)).one()

        statement = insert(Profiles).values(
            {
                Profiles.user_id.key: uuid,
                Profiles.email.key: user.email,
                Profiles.name.key: user.name,
                Profiles.nickname.key: user.nickname,
                Profiles.surname.key: user.surname,
                Profiles.patronymic.key: user.patronymic,
            }
        )

        await self._session.execute(statement)

        return uuid
