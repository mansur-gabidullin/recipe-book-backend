from sqlalchemy.ext.asyncio import create_async_engine

from settings import settings as s

DATABASE_URL = f"postgresql+asyncpg://{s.db_user}:{s.db_password}@{s.db_host}:{s.db_port}/{s.db_name}"

async_engine = create_async_engine(DATABASE_URL)
