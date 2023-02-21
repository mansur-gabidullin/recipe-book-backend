from uuid import UUID

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.users.interfaces.access_token_creator import IAccessTokenCreator
from application_core.users.interfaces.add_user_command import IAddUserCommand
from application_core.users.interfaces.password_hasher import IPasswordHasher
from application_core.users.interfaces.token import IToken
from application_core.users.interfaces.user import IUser
from application_core.users.interfaces.user_result import IUserResult
from application_core.users.interfaces.users_query import IUsersQuery
from application_core.users.interfaces.users_repository import IUsersRepository
from application_core.users.interfaces.users_service import IUsersService
from application_core.users.interfaces.users_service_converter import IUsersServiceConverter
from application_core.users.converters.users_service_converter import UsersServiceConverter
from application_core.users.services.users import UsersService

from infrastructure.access_token_creator import AccessTokenCreator
from infrastructure.password_hasher import PasswordHasher
from infrastructure.repositories.users import UsersRepository
from infrastructure.session import current_session

from presentation.interfaces.users_converter import IUsersConverter
from presentation.beans.add_user_command import AddUserCommand
from presentation.beans.remove_user_command import RemoveUserCommand
from presentation.beans.token import Token
from presentation.beans.users_query import UsersQuery
from presentation.converters.users_service import UsersConverter
from presentation.exceptions import credentials_exception

from settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/token")


async def create_users_query(login: str = None, limit: int = None) -> IUsersQuery:
    return UsersQuery(login=login, limit=limit)


async def create_add_user_command(
    login: str,
    password: str,
    password_confirm: str,
    email: EmailStr,
    name: str = None,
    nickname: str = None,
    surname: str = None,
    patronymic: str = None,
) -> IAddUserCommand:
    return AddUserCommand(
        login=login,
        password=password,
        password_confirm=password_confirm,
        email=email,
        name=name,
        nickname=nickname,
        surname=surname,
        patronymic=patronymic,
    )


async def create_remove_user_command(uuid: UUID):
    return RemoveUserCommand(uuid=uuid)


async def create_users_converter() -> IUsersConverter:
    return UsersConverter()


async def create_database_session() -> AsyncSession:
    return current_session


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


async def create_access_token_creator() -> IAccessTokenCreator:
    return AccessTokenCreator(
        secret_key=settings.access_token_secret_key,
        algorithm=settings.access_token_algorithm,
        expires_minutes=settings.access_token_expire_minutes,
    )


async def create_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    token_creator: IAccessTokenCreator = Depends(create_access_token_creator),
) -> IToken:
    try:
        access_token = await token_creator.create(data={"sub": form_data.username})
        return Token(access_token=access_token, token_type="bearer")
    except Exception:
        raise credentials_exception


def check_access_token_exists(token: str = Depends(oauth2_scheme)) -> None:
    if not token:
        raise credentials_exception


async def authenticate_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    repository: IUsersRepository = Depends(create_users_repository),
    passwordHasher: IPasswordHasher = Depends(create_password_hasher),
) -> None:
    user: IUserResult | None
    [user] = await repository.get_users(UsersQuery(login=form_data.username, limit=1))

    if (
        not user
        or user.is_removed
        or not user.is_active
        or not await passwordHasher.verify(user.password_hash, form_data.password)
    ):
        raise credentials_exception


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    token_creator: IAccessTokenCreator = Depends(create_access_token_creator),
    user_service: IUsersService = Depends(create_users_service),
) -> IUser:
    try:
        payload = await token_creator.read(token)
        login: str = payload.get("sub")

        if login is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception

    user: IUser | None
    [user] = await user_service.get_users_list(UsersQuery(login=login, limit=1))

    if not user or user.is_removed:
        raise credentials_exception

    return user


async def get_current_active_user(current_user: IUser = Depends(get_current_user)) -> IUser:
    if not current_user.is_active:
        raise credentials_exception
    return current_user
