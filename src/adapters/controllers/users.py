from beans.dtos.user import UserDTO
from beans.queries.users_list import UsersListQuery
from ports.primary import IUsersService


class UsersController:
    def __init__(self, service: IUsersService):
        self._service = service

    async def get_users_list(self, query: UsersListQuery) -> list[UserDTO]:
        return await self._service.execute(query)
