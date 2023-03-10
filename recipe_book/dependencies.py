from uuid import UUID

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.users.interfaces.access_token_creator import ITokenCreator
from application_core.users.interfaces.add_user_command import IAddUserCommand
from application_core.users.interfaces.password_hasher import IPasswordHasher
from application_core.users.interfaces.users_query import IUsersQuery
from application_core.users.interfaces.users_repository import IUsersRepository
from application_core.users.interfaces.users_service import IUsersService
from application_core.users.interfaces.users_service_converter import IUsersServiceConverter

from application_core.users.converters.users_service_converter import UsersServiceConverter
from application_core.users.services.users import UsersService

from infrastructure.access_token_creator import TokenCreator
from infrastructure.password_hasher import PasswordHasher
from infrastructure.repositories.users import UsersRepository
from infrastructure.session import AsyncScopedSession

from presentation.interfaces.users_converter import IUsersConverter

from presentation.beans.add_user_command import AddUserCommand
from presentation.beans.remove_user_command import RemoveUserCommand
from presentation.beans.users_query import UsersQuery
from presentation.converters.users_service import UsersConverter

from settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/token", auto_error=False)


async def create_users_query(login: str = None, limit: int = None) -> IUsersQuery:
    return UsersQuery(login=login, limit=limit)


async def create_add_user_command(addUserCommand: AddUserCommand) -> IAddUserCommand:
    return addUserCommand


async def create_remove_user_command(uuid: UUID):
    return RemoveUserCommand(uuid=uuid)


async def create_users_converter() -> IUsersConverter:
    return UsersConverter()


async def create_database_session() -> AsyncSession:
    async with AsyncScopedSession() as session:
        async with session.begin():
            yield session
    await AsyncScopedSession.remove()


async def create_users_repository(session: AsyncSession = Depends(create_database_session)) -> IUsersRepository:
    return UsersRepository(session)


async def create_password_hasher() -> IPasswordHasher:
    return PasswordHasher()


async def create_users_service_converter() -> IUsersServiceConverter:
    return UsersServiceConverter()


async def create_users_service(
    repository: IUsersRepository = Depends(create_users_repository),
    converter: IUsersServiceConverter = Depends(create_users_service_converter),
    passwordHasher: IPasswordHasher = Depends(create_password_hasher),
) -> IUsersService:
    return UsersService(repository, converter, passwordHasher)


async def create_token_creator() -> ITokenCreator:
    return TokenCreator(
        secret_key=settings.token_secret_key,
        algorithm=settings.token_algorithm,
        csrf_expire_minutes=settings.csrf_token_expire_minutes,
        access_expire_minutes=settings.access_token_expire_minutes,
        refresh_expire_days=settings.refresh_token_expire_days,
    )
