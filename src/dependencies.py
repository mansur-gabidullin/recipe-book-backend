from fastapi import Depends

from application_core.bounded_contexts.users.beans.queries.users_list import UsersListQuery
from application_core.bounded_contexts.users.ports.primary import IUsersService, IUsersController
from application_core.bounded_contexts.users.ports.secondary import IDatabaseSession, IUsersRepository
from application_core.bounded_contexts.users.use_cases.users_service import UsersService
from infrastructure.adapters.repositories.users import UsersRepository
from infrastructure.database_sqlalchemy.session import AsyncScopedSession
from presentation.adapters.controllers.users import UsersController


async def users_query_factory() -> UsersListQuery:
    return UsersListQuery()


async def database_session_factory() -> IDatabaseSession:
    return AsyncScopedSession()


async def users_repository_factory(session: IDatabaseSession = Depends(database_session_factory)) -> IUsersRepository:
    return UsersRepository(session)


async def users_service_factory(repository: IUsersRepository = Depends(users_repository_factory)) -> IUsersService:
    return UsersService(repository)


async def users_controller_factory(service: IUsersService = Depends(users_service_factory)) -> IUsersController:
    return UsersController(service)
