from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.bounded_contexts.users.beans.queries.users import UsersQuery
from application_core.bounded_contexts.users.ports.primary import IAdministratorUseCase, IUsersController
from application_core.bounded_contexts.users.ports.secondary import IUsersRepository
from application_core.bounded_contexts.users.services.administrator import AdministratorUseCase

from infrastructure.adapters.users.repositories.users import UsersRepository
from infrastructure.database_sqlalchemy.session import AsyncScopedSession

from presentation.adapters.users.controllers.users import UsersController


async def users_query_factory() -> UsersQuery:
    return UsersQuery()


async def database_session_factory() -> AsyncSession:
    return AsyncScopedSession()


async def users_repository_factory(session: AsyncSession = Depends(database_session_factory)) -> IUsersRepository:
    return UsersRepository(session)


async def administrator_use_case_factory(
        repository: IUsersRepository = Depends(users_repository_factory)) -> IAdministratorUseCase:
    return AdministratorUseCase(repository)


async def users_controller_factory(
        admin_service: IAdministratorUseCase = Depends(administrator_use_case_factory)) -> IUsersController:
    return UsersController(admin_service)
