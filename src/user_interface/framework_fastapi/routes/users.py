from fastapi import APIRouter, Depends

from beans.dtos.user import UserDTO
from beans.queries.users_list import UsersListQuery
from ports.primary import IUsersController
from shared_kernel.dependencies import users_query_factory, users_controller_factory

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/', response_model=list[UserDTO])
async def get_root(
        controller: IUsersController = Depends(users_controller_factory),
        query: UsersListQuery = Depends(users_query_factory)
) -> list[UserDTO]:
    return await controller.get_users_list(query)
