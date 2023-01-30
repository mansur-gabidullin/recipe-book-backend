from application_core.bounded_contexts.users.beans.add_user_command_dto import AddUserCommandDTO
from application_core.bounded_contexts.users.beans.add_user_result_dto import AddUserResultDTO
from application_core.bounded_contexts.users.beans.user_dto import UserDTO
from application_core.bounded_contexts.users.beans.users_query_dto import UsersQueryDTO
from application_core.bounded_contexts.users.ports.primary import IAdministratorUseCase


class UsersController:
    def __init__(self, admin_service: IAdministratorUseCase):
        self._admin_service = admin_service

    async def get_users_list(self, query: UsersQueryDTO) -> list[UserDTO]:
        return await self._admin_service.fetch_users(query)

    async def add_user(self, command: AddUserCommandDTO) -> AddUserResultDTO:
        return await self._admin_service.add_user(command)
