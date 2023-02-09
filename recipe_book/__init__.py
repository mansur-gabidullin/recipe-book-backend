def create_env():
    from os.path import isfile
    from shutil import copy

    if not isfile("recipe_book/.env") and isfile("recipe_book/.env.example"):
        copy("recipe_book/.env.example", "recipe_book/.env")


def init_db():
    import os

    if os.getcwd().endswith("/recipe-book-backend"):
        os.chdir("recipe_book")

    import asyncio

    from infrastructure.database_sqlalchemy.engine import engine
    from infrastructure.database_sqlalchemy.tables.base import Base

    # this imports needs for Base.metadata.create_all while running init_db script
    # noinspection PyUnresolvedReferences
    from infrastructure.database_sqlalchemy.tables.users import (
        groups,
        permissions,
        profiles,
        roles,
        roles_permissions,
        users,
        users_groups,
    )

    async def init_models():
        async with engine.connect() as connection:
            async with connection.begin():
                await connection.run_sync(Base.metadata.drop_all)
                await connection.run_sync(Base.metadata.create_all)

    asyncio.run(init_models())


def start():
    import os

    if os.getcwd().endswith("/recipe-book-backend"):
        os.chdir("recipe_book")

    import uvicorn
    from settings import settings

    uvicorn.run(
        "presentation.framework_fastapi.app:app",
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
