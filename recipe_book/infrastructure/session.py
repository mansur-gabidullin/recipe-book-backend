from asyncio import current_task

from sqlalchemy.ext.asyncio import async_scoped_session, async_sessionmaker, AsyncSession

from .engine import async_engine

AsyncScopedSession = async_scoped_session(async_sessionmaker(async_engine, class_=AsyncSession), scopefunc=current_task)
