import asyncio
from uuid import UUID

from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.users.interfaces.remove_user_command import IRemoveUserCommand
from application_core.users.interfaces.user_data import IUserData
from application_core.users.interfaces.user_result import IUserResult
from application_core.users.interfaces.users_query import IUsersQuery
from application_core.users.interfaces.users_repository import IUsersRepository

from ..beans.profile_result import ProfileResult
from ..beans.user_result import UserResult
from ..helpers import scalar_as_dict
from ..tables.users.profiles import Profiles
from ..tables.users.users import Users


class UsersRepository(IUsersRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_users(self, query_query: IUsersQuery) -> list[IUserResult]:
        result = []
        statement = select(Users, Profiles).join_from(Users, Profiles, full=True)

        if query_query.login:
            statement = statement.where(Users.login == query_query.login)

        if query_query.limit:
            statement = statement.limit(query_query.limit)

        for item in (await self._session.execute(statement)).mappings():
            profile = ProfileResult(**scalar_as_dict(item.Profiles)) if item.Profiles else None
            result.append(UserResult(**scalar_as_dict(item.Users), profile=profile))

        return result

    async def add_user(self, user_data: IUserData) -> UUID:
        statement = (
            insert(Users)
            .values(
                {
                    Users.login.key: user_data.login,
                    Users.password_hash.key: user_data.password_hash,
                    Users.is_active.key: user_data.is_active,
                }
            )
            .returning(Users.uuid)
        )

        [uuid] = (await self._session.execute(statement)).one()

        if user_data.email:
            statement = insert(Profiles).values(
                {
                    Profiles.user_uuid.key: uuid,
                    Profiles.email.key: user_data.email,
                    Profiles.name.key: user_data.name,
                    Profiles.nickname.key: user_data.nickname,
                    Profiles.surname.key: user_data.surname,
                    Profiles.patronymic.key: user_data.patronymic,
                }
            )

            await self._session.execute(statement)

        return uuid

    async def remove_user(self, remove_user_command: IRemoveUserCommand) -> None:
        # todo: prevent delete last active admin user

        update_statement = (
            update(Users).where(Users.uuid == remove_user_command.uuid).values({Users.is_removed.key: True})
        )

        delete_statement = delete(Profiles).where(Profiles.user_uuid == remove_user_command.uuid)

        await asyncio.gather(self._session.execute(update_statement), self._session.execute(delete_statement))
