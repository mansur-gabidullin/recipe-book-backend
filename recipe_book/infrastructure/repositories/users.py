import asyncio
from uuid import UUID

from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.users.interfaces.remove_user_command import IRemoveUserCommand
from application_core.users.interfaces.user_add_data import IAddUserData
from application_core.users.interfaces.user_record import IUserRecord
from application_core.users.interfaces.users_query import IUsersQuery
from application_core.users.interfaces.users_repository import IUsersRepository

from ..interfaces.user_converter import IUserRecordConverter
from ..tables.users.profiles import Profiles
from ..tables.users.users import Users


class UsersRepository(IUsersRepository):
    def __init__(
        self,
        session: AsyncSession,
        converter: IUserRecordConverter,
    ):
        self._session = session
        self._converter = converter
        self._join_statement = select(Users, Profiles).join_from(Users, Profiles, full=True)

    async def get_users(self, query_query: IUsersQuery) -> list[IUserRecord]:
        statement = self._join_statement.where(Users.is_removed == query_query.is_removed)

        if query_query.login:
            statement = statement.where(Users.login == query_query.login)

        if query_query.login:
            statement = statement.where(Users.login == query_query.login)

        if query_query.limit:
            statement = statement.limit(query_query.limit)

        return self._converter.from_users_results(await self._session.execute(statement))

    async def get_user_by_login(self, login: str) -> IUserRecord:
        statement = self._join_statement.where(Users.login == login).limit(1)

        user: IUserRecord | None
        [user] = self._converter.from_users_results(await self._session.execute(statement))

        return user

    async def get_user_by_uuid(self, uuid: UUID) -> IUserRecord:
        statement = self._join_statement.where(Users.uuid == uuid).limit(1)

        user: IUserRecord | None
        [user] = self._converter.from_users_results(await self._session.execute(statement))

        return user

    async def add_user(self, user_data: IAddUserData) -> UUID:
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
                    Profiles.phone_number.key: user_data.phone_number,
                    Profiles.name.key: user_data.name,
                    Profiles.nickname.key: user_data.nickname,
                    Profiles.surname.key: user_data.surname,
                    Profiles.patronymic.key: user_data.patronymic,
                }
            )

            await self._session.execute(statement)

        return uuid

    async def remove_user(self, remove_user_command: IRemoveUserCommand) -> None:
        update_statement = (
            update(Users).where(Users.uuid == remove_user_command.uuid).values({Users.is_removed.key: True})
        )

        delete_statement = delete(Profiles).where(Profiles.user_uuid == remove_user_command.uuid)

        await asyncio.gather(self._session.execute(update_statement), self._session.execute(delete_statement))
