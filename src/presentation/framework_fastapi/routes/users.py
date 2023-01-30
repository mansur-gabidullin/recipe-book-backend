from fastapi import APIRouter, Depends

from application_core.bounded_contexts.users.beans.dtos.user import UserDTO
from application_core.bounded_contexts.users.beans.queries.users import UsersQuery
from application_core.bounded_contexts.users.ports.primary import IUsersController

from factories import users_controller_factory, users_query_factory

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/', response_model=list[UserDTO])
async def get_users_list(
        controller: IUsersController = Depends(users_controller_factory),
        query: UsersQuery = Depends(users_query_factory)
) -> list[UserDTO]:
    return await controller.get_users_list(query)
