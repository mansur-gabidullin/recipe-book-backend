from uuid import UUID

from fastapi import APIRouter, Depends

from application_core.bounded_contexts.users.beans.commands.remove_user_command_dto import RemoveUserCommandDTO
from application_core.bounded_contexts.users.beans.queries.users_query_dto import UsersQueryDTO
from application_core.bounded_contexts.users.beans.commands.register_user_command_dto import RegisterUserCommandDTO
from application_core.bounded_contexts.users.beans.results.register_user_result_dto import RegisterUserResultDTO
from application_core.bounded_contexts.users.beans.user_dto import UserDTO
from application_core.bounded_contexts.users.ports.primary import IAdminPanelController

from ..dependencies import users_controller_factory, users_query_factory

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserDTO])
async def endpoint_for_receiving_list_of_users(
    controller: IAdminPanelController = Depends(users_controller_factory),
    query: UsersQueryDTO = Depends(users_query_factory),
) -> list[UserDTO]:
    return await controller.get_users_list(query)


@router.post("/", response_model=RegisterUserResultDTO)
async def endpoint_for_creating_user(
    command: RegisterUserCommandDTO,
    controller: IAdminPanelController = Depends(users_controller_factory),
) -> RegisterUserResultDTO:
    return await controller.add_user(command)


@router.delete("/{uuid}")
async def endpoint_for_creating_user(
    uuid: UUID,
    controller: IAdminPanelController = Depends(users_controller_factory),
) -> None:
    command = RemoveUserCommandDTO(uuid=uuid)
    return await controller.remove_user(command)
