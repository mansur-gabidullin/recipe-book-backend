import asyncio

from infrastructure.database_sqlalchemy.engine import engine
from infrastructure.database_sqlalchemy.tables.base import metadata


def run():
    async def init_models():
        async with engine.begin() as conn:
            await conn.run_sync(metadata.drop_all)
            await conn.run_sync(metadata.create_all)

    asyncio.run(init_models())
