from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.bounded_contexts.users.beans.queries.users_query_dto import UsersQueryDTO
from application_core.bounded_contexts.users.beans.user_dto import UserDTO
from application_core.bounded_contexts.users.ports.primary import IAdministratorUseCase, IAdminPanelController
from application_core.bounded_contexts.users.ports.secondary import (
    IUsersRepository,
    IPasswordHasher,
    IAccessTokenCreator,
)
from application_core.bounded_contexts.users.use_cases.admin import UsersAdminUseCase

from infrastructure.access_token_creator import AccessTokenCreator
from infrastructure.adapters.users.repositories.users import UsersRepository
from infrastructure.database_sqlalchemy.session import current_session
from infrastructure.password_hasher import PasswordHasher

from presentation.adapters.users.controllers.admin_panel import AdminPanelController
from presentation.framework_fastapi.exceptions import credentials_exception

from settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/token")


async def users_query_factory() -> UsersQueryDTO:
    return UsersQueryDTO()


async def database_session_factory() -> AsyncSession:
    return current_session


async def users_repository_factory(session: AsyncSession = Depends(database_session_factory)) -> IUsersRepository:
    return UsersRepository(session)


async def password_hasher_factory() -> IPasswordHasher:
    return PasswordHasher()


async def access_token_creator_factory() -> IAccessTokenCreator:
    return AccessTokenCreator(
        secret_key=settings.access_token_secret_key,
        algorithm=settings.access_token_algorithm,
        expires_minutes=settings.access_token_expire_minutes,
    )


async def admin_use_case_factory(
    repository: IUsersRepository = Depends(users_repository_factory),
    passwordHasher: IPasswordHasher = Depends(password_hasher_factory),
) -> IAdministratorUseCase:
    return UsersAdminUseCase(repository, passwordHasher)


async def users_controller_factory(
    admin_service: IAdministratorUseCase = Depends(admin_use_case_factory),
) -> IAdminPanelController:
    return AdminPanelController(admin_service)


async def authenticate_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    repository: IUsersRepository = Depends(users_repository_factory),
    passwordHasher: IPasswordHasher = Depends(password_hasher_factory),
) -> None:
    user = (await repository.get_users(UsersQueryDTO(login=form_data.username, limit=1)))[0]

    if (
        not user
        or user.is_removed
        or not user.is_active
        or not await passwordHasher.verify(user.password_hash, form_data.password)
    ):
        raise credentials_exception


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    token_creator: IAccessTokenCreator = Depends(access_token_creator_factory),
    user_service: IAdministratorUseCase = Depends(admin_use_case_factory),
) -> UserDTO:
    try:
        payload = await token_creator.read(token)
        login: str = payload.get("sub")

        if login is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception

    user = (await user_service.handle_users_query(UsersQueryDTO(login=login, limit=1)))[0]

    if not user or user.is_removed:
        raise credentials_exception

    return user


async def get_current_active_user(current_user: UserDTO = Depends(get_current_user)) -> UserDTO:
    if not current_user.is_active:
        raise credentials_exception
    return current_user
