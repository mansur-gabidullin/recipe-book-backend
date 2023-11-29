from uuid import UUID

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.bin.interfaces.bin_repository import IBinRepository

from ..tables.users.users import Users


class BinRepository[T](IBinRepository[T]):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def restore(self, uuid: UUID):
        statement = update(Users).where(Users.uuid == uuid).values({Users.is_removed.key: False})
        await self._session.execute(statement)
