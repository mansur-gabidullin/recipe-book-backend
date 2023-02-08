from dataclasses import asdict

from ..beans.user_po import UserPO
from ..beans.add_user_command_dto import AddUserCommandDTO
from ..beans.user_dto import UserDTO
from ..beans.users_query_dto import UsersQueryDTO
from ..beans.add_user_result_dto import AddUserResultDTO
from ..entities.user import UserEntity
from ..ports.primary import IAdministratorUseCase
from ..ports.secondary import IUsersRepository


class UsersAdminUseCase(IAdministratorUseCase):
    def __init__(self, repository: IUsersRepository):
        self._repository = repository

    async def handle_users_query(self, query: UsersQueryDTO) -> list[UserDTO]:
        return [UserDTO(**asdict(user)) for user in await self._repository.get_users(query)]

    async def handle_add_user_command(self, command: AddUserCommandDTO) -> AddUserResultDTO:
        try:
            password_solt, password_hash = UserEntity.generate_password()

            user = UserPO(**command.dict(), password_solt=password_solt, password_hash=password_hash)
        except Exception as e:
            print(e)
            raise e

        return AddUserResultDTO(id=await self._repository.add_user(user))
