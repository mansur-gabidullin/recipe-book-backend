from sqlalchemy import insert


def check_dir():
    import os

    if os.getcwd().endswith("/recipe-book-backend"):
        os.chdir("recipe_book")


def create_env():
    from os.path import isfile
    from secrets import token_hex

    secret_key_prefix = "TOKEN_SECRET_KEY"
    env_example_file_name = ".env.example"

    if not isfile(".env") and isfile(f"{env_example_file_name}"):
        with open(f"{env_example_file_name}", "rt", encoding="utf-8") as input_:
            with open(".env", "wt", encoding="utf-8") as output:
                for line in input_.readlines():
                    new_line = (
                        line.replace(f"{secret_key_prefix}=", f"{secret_key_prefix}={token_hex(32)}")
                        if line.startswith(f"{secret_key_prefix}=")
                        else line
                    )
                    output.write(new_line)


def init_db():
    check_dir()

    import asyncio

    from infrastructure.engine import async_engine
    from infrastructure.tables.base import Base

    # this imports needs for Base.metadata.create_all while running init_db script
    # noinspection PyUnresolvedReferences
    from infrastructure.tables.users import (
        groups,
        permissions,
        profiles,
        roles,
        roles_permissions,
        users,
        users_groups,
    )

    # noinspection PyUnresolvedReferences
    from infrastructure.tables.products import products

    # noinspection PyUnresolvedReferences
    from infrastructure.tables.recipes import ingredients, cooking_steps, recipes

    async def init_models():
        check_dir()

        from settings import settings
        from infrastructure.tables.users.users import Users
        from infrastructure.password_hasher import PasswordHasher

        async with async_engine.connect() as connection:
            async with connection.begin():
                await connection.run_sync(Base.metadata.drop_all)
                await connection.run_sync(Base.metadata.create_all)

                statement = (
                    insert(Users)
                    .values(
                        {
                            "login": settings.super_user_login,
                            "password_hash": await PasswordHasher().hash(settings.super_user_password),
                            "is_active": True,
                        }
                    )
                    .returning(Users.uuid)
                )

                await connection.execute(statement)

    asyncio.run(init_models())


def start():
    check_dir()

    import uvicorn
    from settings import settings

    uvicorn.run(
        "presentation.app:app",
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
