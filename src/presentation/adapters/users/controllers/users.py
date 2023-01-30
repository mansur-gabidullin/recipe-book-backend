from application_core.bounded_contexts.users.beans.dtos.user import UserDTO
from application_core.bounded_contexts.users.beans.queries.users import UsersQuery
from application_core.bounded_contexts.users.ports.primary import IAdministratorUseCase


class UsersController:
    def __init__(self, admin_service: IAdministratorUseCase):
        self._admin_service = admin_service

    async def get_users_list(self, query: UsersQuery) -> list[UserDTO]:
        return await self._admin_service.fetch_users(query)
