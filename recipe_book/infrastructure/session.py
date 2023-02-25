from asyncio import current_task

from sqlalchemy.ext.asyncio import async_scoped_session, async_sessionmaker

from .engine import async_engine

async_session_factory = async_sessionmaker(async_engine)
AsyncScopedSession = async_scoped_session(async_session_factory, scopefunc=current_task)
