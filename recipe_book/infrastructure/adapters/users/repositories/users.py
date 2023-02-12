import asyncio
from uuid import UUID

from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.bounded_contexts.users.aggregates.profile import ProfileEntity
from application_core.bounded_contexts.users.beans.user_po import UserPO
from application_core.bounded_contexts.users.beans.queries.users_query_dto import UsersQueryDTO
from application_core.bounded_contexts.users.aggregates.user import UserEntity
from application_core.bounded_contexts.users.ports.secondary import IUsersRepository

from ....database_sqlalchemy.helpers import scalar_as_dict
from ....database_sqlalchemy.tables.users.profiles import Profiles
from ....database_sqlalchemy.tables.users.users import Users


class UsersRepository(IUsersRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_users(self, query: UsersQueryDTO) -> list[UserEntity]:
        # todo: limits, pagination from query
        print(f"query = {query}")

        result = []
        statement = select(Users, Profiles).join_from(Users, Profiles, full=True)

        print(statement)

        for item in (await self._session.execute(statement)).mappings():
            profile = ProfileEntity(**scalar_as_dict(item.Profiles)) if item.Profiles else None
            result.append(UserEntity(**scalar_as_dict(item.Users), profile=profile))

        return result

    async def add_user(self, user: UserPO) -> UUID:
        match user.dict():
            case {
                "login": login,
                "password_hash": password_hash,
                "email": email,
                "name": name,
                "nickname": nickname,
                "surname": surname,
                "patronymic": patronymic,
            }:
                statement = (
                    insert(Users)
                    .values(
                        {
                            Users.login.key: login,
                            Users.password_hash.key: password_hash,
                        }
                    )
                    .returning(Users.uuid)
                )

                (uuid,) = (await self._session.execute(statement)).one()

                if email:
                    statement = insert(Profiles).values(
                        {
                            Profiles.user_uuid.key: uuid,
                            Profiles.email.key: email,
                            Profiles.name.key: name,
                            Profiles.nickname.key: nickname,
                            Profiles.surname.key: surname,
                            Profiles.patronymic.key: patronymic,
                        }
                    )

                    await self._session.execute(statement)

                return uuid

            case _:
                raise TypeError("argument user is at wrong type")

    async def remove_user(self, uuid: UUID) -> None:
        update_statement = update(Users).where(Users.uuid == uuid).values({Users.is_removed.key: True})
        delete_statement = delete(Profiles).where(Profiles.user_uuid == uuid)

        await asyncio.gather(self._session.execute(update_statement), self._session.execute(delete_statement))
