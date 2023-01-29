from application_core.bounded_contexts.users.beans.dtos.user import UserDTO
from application_core.bounded_contexts.users.beans.queries.users_list import UsersListQuery
from application_core.bounded_contexts.users.ports.primary import IUsersService


class UsersController:
    def __init__(self, service: IUsersService):
        self._service = service

    async def get_users_list(self, query: UsersListQuery) -> list[UserDTO]:
        return await self._service.execute(query)
