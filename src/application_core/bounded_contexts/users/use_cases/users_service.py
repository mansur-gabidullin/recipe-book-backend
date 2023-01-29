from ..beans.dtos.user import UserDTO
from ..beans.queries.users_list import UsersListQuery
from ..ports.secondary import IUsersRepository


class UsersService:
    def __init__(self, repository: IUsersRepository):
        self._repository = repository

    async def execute(self, query: UsersListQuery) -> list[UserDTO]:
        return await self._repository.get_users_list(query)
