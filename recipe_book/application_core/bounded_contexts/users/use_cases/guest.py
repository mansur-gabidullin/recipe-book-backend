from ..beans.commands.register_user_command_dto import RegisterUserCommandDTO
from ..beans.results.register_user_result_dto import RegisterUserResultDTO
from ..beans.user_po import UserPO
from ..entities.user import UserEntity
from ..ports.primary import IGuestUseCase
from ..ports.secondary import IUsersRepository


class UsersGuestUseCase(IGuestUseCase):
    def __init__(self, repository: IUsersRepository):
        self._repository = repository

    async def handle_register_command(self, command: RegisterUserCommandDTO) -> RegisterUserResultDTO:
        try:
            user = UserPO(**command.dict(), password_hash=UserEntity.generate_password_hash(command.password))
            return RegisterUserResultDTO(uuid=await self._repository.add_user(user))
        except Exception as e:
            # todo: validation errors
            # todo: logging
            print(e)
            raise e
