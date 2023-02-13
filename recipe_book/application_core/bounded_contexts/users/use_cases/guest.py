from ..beans.commands.register_user_command_dto import RegisterUserCommandDTO
from ..beans.results.register_user_result_dto import RegisterUserResultDTO
from ..beans.user_po import UserPO
from ..ports.primary import IGuestUseCase
from ..ports.secondary import IUsersRepository, IPasswordHasher


class UsersGuestUseCase(IGuestUseCase):
    def __init__(self, repository: IUsersRepository, password_hasher: IPasswordHasher):
        self._repository = repository
        self._password_hasher = password_hasher

    async def handle_register_command(self, command: RegisterUserCommandDTO) -> RegisterUserResultDTO:
        try:
            user = UserPO(
                **command.dict(), is_active=True, password_hash=await self._password_hasher.hash(command.password)
            )
            return RegisterUserResultDTO(uuid=await self._repository.add_user(user))
        except Exception as error:
            # todo: validation errors
            # todo: logging
            raise error
