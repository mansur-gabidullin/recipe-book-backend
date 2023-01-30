from ..beans.dtos.user import UserDTO
from ..beans.queries.users import UsersQuery
from ..ports.secondary import IUsersRepository


class AdministratorUseCase:
    def __init__(self, repository: IUsersRepository):
        self._repository = repository

    async def fetch_users(self, query: UsersQuery) -> list[UserDTO]:
        return await self._repository.get_users(query)
