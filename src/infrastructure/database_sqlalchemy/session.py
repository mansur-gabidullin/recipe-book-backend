from asyncio import current_task

from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, async_sessionmaker

from .engine import engine

async_session_factory = async_sessionmaker(engine, class_=AsyncSession)
AsyncScopedSession = async_scoped_session(async_session_factory, scopefunc=current_task)
