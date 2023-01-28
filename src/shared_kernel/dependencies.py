from fastapi import Depends

from adapters.controllers.users import UsersController
from adapters.repositories.users import UsersRepository
from application_core.bounded_contexts.users.use_cases.users_service import UsersService
from beans.queries.users_list import UsersListQuery
from infrastructure.database_sqlalchemy.session import AsyncScopedSession
from ports.primary import IUsersService, IUsersController
from ports.secondary import IUsersRepository, IDatabaseSession


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
