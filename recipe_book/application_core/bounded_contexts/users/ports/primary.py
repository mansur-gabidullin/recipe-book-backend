from typing import Protocol

from ..beans.add_user_command_dto import AddUserCommandDTO
from ..beans.add_user_result_dto import AddUserResultDTO
from ..beans.guest_register_command_dto import GuestRegisterCommandDTO
from ..beans.guest_register_result_dto import GuestRegisterResultDTO
from ..beans.user_dto import UserDTO
from ..beans.users_query_dto import UsersQueryDTO


class IUsersController(Protocol):
    async def get_users_list(self, query: UsersQueryDTO) -> list[UserDTO]:
        ...

    async def add_user(self, command: AddUserCommandDTO) -> AddUserResultDTO:
        ...


class IGuestUseCase(Protocol):
    async def handle_register_command(self, command: GuestRegisterCommandDTO) -> GuestRegisterResultDTO:
        ...


class IAdministratorUseCase(Protocol):
    async def handle_users_query(self, query: UsersQueryDTO) -> list[UserDTO]:
        ...

    async def handle_add_user_command(self, command: AddUserCommandDTO) -> AddUserResultDTO:
        ...
