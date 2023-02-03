from fastapi import APIRouter, Depends

from application_core.bounded_contexts.users.beans.add_user_command_dto import AddUserCommandDTO
from application_core.bounded_contexts.users.beans.add_user_result_dto import AddUserResultDTO
from application_core.bounded_contexts.users.beans.user_dto import UserDTO
from application_core.bounded_contexts.users.beans.users_query_dto import UsersQueryDTO
from application_core.bounded_contexts.users.ports.primary import IUsersController

from ..dependencies import users_controller_factory, users_query_factory

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/', response_model=list[UserDTO])
async def endpoint_for_receiving_list_of_users(
        controller: IUsersController = Depends(users_controller_factory),
        query: UsersQueryDTO = Depends(users_query_factory)
) -> list[UserDTO]:
    return await controller.get_users_list(query)


@router.post('/', response_model=AddUserResultDTO)
async def endpoint_for_creating_user(
        command: AddUserCommandDTO,
        controller: IUsersController = Depends(users_controller_factory),
) -> AddUserResultDTO:
    return await controller.add_user(command)
