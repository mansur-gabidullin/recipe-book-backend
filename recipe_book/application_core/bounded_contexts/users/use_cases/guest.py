from ..beans.guest_register_command_dto import GuestRegisterCommandDTO
from ..beans.guest_register_result_dto import GuestRegisterResultDTO
from ..ports.primary import IGuestUseCase
from ..ports.secondary import IUsersRepository


class UsersGuestUseCase(IGuestUseCase):
    def __init__(self, repository: IUsersRepository):
        self._repository = repository

    async def handle_register_command(self, command: GuestRegisterCommandDTO) -> GuestRegisterResultDTO:
        ...
