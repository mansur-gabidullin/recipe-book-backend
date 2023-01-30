from ..beans.user_po import UserPO
from ..beans.add_user_command_dto import AddUserCommandDTO
from ..beans.user_dto import UserDTO
from ..beans.users_query_dto import UsersQueryDTO
from ..beans.add_user_result_dto import AddUserResultDTO
from ..ports.secondary import IUsersRepository


class UsersAdminUseCase:
    def __init__(self, repository: IUsersRepository):
        self._repository = repository

    async def fetch_users(self, query: UsersQueryDTO) -> list[UserDTO]:
        return await self._repository.get_users(query)

    async def add_user(self, command: AddUserCommandDTO) -> AddUserResultDTO:
        try:
            user = UserPO(
                **command.dict(),
                password_solt=command.login,
                password_hash=command.login
            )
        except Exception as e:
            print(e)
            raise e

        return await self._repository.add_user(user)
