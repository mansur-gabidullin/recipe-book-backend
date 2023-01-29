import asyncio

from infrastructure.database_sqlalchemy.engine import engine
from infrastructure.database_sqlalchemy.tables.base import Base

# this imports needs for Base.metadata.create_all while running init_db script
from infrastructure.database_sqlalchemy.tables import (
    groups,
    permissions,
    profiles,
    roles,
    roles_permissions,
    users,
    users_groups,
)


def run():
    async def init_models():
        async with engine.connect() as connection:
            async with connection.begin():
                await connection.run_sync(Base.metadata.drop_all)
                await connection.run_sync(Base.metadata.create_all)

    asyncio.run(init_models())
