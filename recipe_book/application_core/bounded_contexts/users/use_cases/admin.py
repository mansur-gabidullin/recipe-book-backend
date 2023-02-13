from dataclasses import asdict

from ..beans.commands.remove_user_command_dto import RemoveUserCommandDTO
from ..beans.queries.users_query_dto import UsersQueryDTO
from ..beans.commands.register_user_command_dto import RegisterUserCommandDTO
from ..beans.results.register_user_result_dto import RegisterUserResultDTO
from ..beans.user_po import UserPO
from ..beans.user_dto import UserDTO
from ..ports.primary import IAdministratorUseCase
from ..ports.secondary import IUsersRepository, IPasswordHasher


class UsersAdminUseCase(IAdministratorUseCase):
    def __init__(self, repository: IUsersRepository, password_hasher: IPasswordHasher):
        self._repository = repository
        self._password_hasher = password_hasher

    async def handle_users_query(self, query: UsersQueryDTO) -> list[UserDTO]:
        return [UserDTO(**asdict(user)) for user in await self._repository.get_users(query)]

    async def handle_add_user_command(self, command: RegisterUserCommandDTO) -> RegisterUserResultDTO:
        try:
            user = UserPO(
                **command.dict(), is_active=True, password_hash=await self._password_hasher.hash(command.password)
            )
            return RegisterUserResultDTO(uuid=await self._repository.add_user(user))
        except Exception as error:
            # todo: validation errors
            # todo: logging
            raise error

    async def handle_remove_user_command(self, command: RemoveUserCommandDTO) -> None:
        return await self._repository.remove_user(command.uuid)
