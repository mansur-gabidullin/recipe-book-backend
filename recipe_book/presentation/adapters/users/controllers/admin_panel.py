from application_core.bounded_contexts.users.beans.commands.register_user_command_dto import RegisterUserCommandDTO
from application_core.bounded_contexts.users.beans.results.register_user_result_dto import RegisterUserResultDTO
from application_core.bounded_contexts.users.beans.user_dto import UserDTO
from application_core.bounded_contexts.users.beans.queries.users_query_dto import UsersQueryDTO
from application_core.bounded_contexts.users.ports.primary import IAdministratorUseCase, IAdminPanelController


class AdminPanelController(IAdminPanelController):
    def __init__(self, admin_service: IAdministratorUseCase):
        self._admin_service = admin_service

    async def get_users_list(self, query: UsersQueryDTO) -> list[UserDTO]:
        return await self._admin_service.handle_users_query(query)

    async def add_user(self, command: RegisterUserCommandDTO) -> RegisterUserResultDTO:
        return await self._admin_service.handle_add_user_command(command)
