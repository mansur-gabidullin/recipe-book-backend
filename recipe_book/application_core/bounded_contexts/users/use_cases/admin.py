from dataclasses import asdict

from ..beans.queries.users_query_dto import UsersQueryDTO
from ..beans.commands.register_user_command_dto import RegisterUserCommandDTO
from ..beans.results.register_user_result_dto import RegisterUserResultDTO
from ..beans.user_po import UserPO
from ..beans.user_dto import UserDTO
from ..entities.user import UserEntity
from ..ports.primary import IAdministratorUseCase
from ..ports.secondary import IUsersRepository


class UsersAdminUseCase(IAdministratorUseCase):
    def __init__(self, repository: IUsersRepository):
        self._repository = repository

    async def handle_users_query(self, query: UsersQueryDTO) -> list[UserDTO]:
        return [UserDTO(**asdict(user)) for user in await self._repository.get_users(query)]

    async def handle_add_user_command(self, command: RegisterUserCommandDTO) -> RegisterUserResultDTO:
        try:
            user = UserPO(**command.dict(), password_hash=UserEntity.generate_password_hash(command.password))
            return RegisterUserResultDTO(uuid=await self._repository.add_user(user))
        except Exception as e:
            # todo: validation errors
            # todo: logging
            print(e)
            raise e
