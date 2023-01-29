from fastapi import APIRouter, Depends

from application_core.bounded_contexts.users.beans.dtos.user import UserDTO
from application_core.bounded_contexts.users.beans.queries.users_list import UsersListQuery
from application_core.bounded_contexts.users.ports.primary import IUsersController
from dependencies import users_controller_factory, users_query_factory

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/', response_model=list[UserDTO])
async def get_root(
        controller: IUsersController = Depends(users_controller_factory),
        query: UsersListQuery = Depends(users_query_factory)
) -> list[UserDTO]:
    return await controller.get_users_list(query)
