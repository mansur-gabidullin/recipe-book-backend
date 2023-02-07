from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.bounded_contexts.users.beans.users_query_dto import UsersQueryDTO
from application_core.bounded_contexts.users.ports.primary import IAdministratorUseCase, IUsersController
from application_core.bounded_contexts.users.ports.secondary import IUsersRepository
from application_core.bounded_contexts.users.use_cases.admin import UsersAdminUseCase

from infrastructure.adapters.users.repositories.users import UsersRepository
from infrastructure.database_sqlalchemy.session import current_session

from presentation.adapters.users.controllers.users import UsersController


async def users_query_factory() -> UsersQueryDTO:
    return UsersQueryDTO()


async def database_session_factory() -> AsyncSession:
    return current_session


async def users_repository_factory(
    session: AsyncSession = Depends(database_session_factory, use_cache=True)
) -> IUsersRepository:
    return UsersRepository(session)


async def admin_use_case_factory(
    repository: IUsersRepository = Depends(users_repository_factory),
) -> IAdministratorUseCase:
    return UsersAdminUseCase(repository)


async def users_controller_factory(
    admin_service: IAdministratorUseCase = Depends(admin_use_case_factory),
) -> IUsersController:
    return UsersController(admin_service)
