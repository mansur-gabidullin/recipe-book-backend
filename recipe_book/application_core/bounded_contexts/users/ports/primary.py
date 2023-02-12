from typing import Protocol

from ..beans.commands.register_user_command_dto import RegisterUserCommandDTO
from ..beans.commands.remove_user_command_dto import RemoveUserCommandDTO
from ..beans.results.register_user_result_dto import RegisterUserResultDTO
from ..beans.queries.users_query_dto import UsersQueryDTO
from ..beans.user_dto import UserDTO


class IAdminPanelController(Protocol):
    async def get_users_list(self, query: UsersQueryDTO) -> list[UserDTO]:
        ...

    async def add_user(self, command: RegisterUserCommandDTO) -> RegisterUserResultDTO:
        ...

    async def remove_user(self, command: RemoveUserCommandDTO) -> None:
        ...


class IGuestUseCase(Protocol):
    async def handle_register_command(self, command: RegisterUserCommandDTO) -> RegisterUserResultDTO:
        ...


class IAdministratorUseCase(Protocol):
    async def handle_users_query(self, query: UsersQueryDTO) -> list[UserDTO]:
        ...

    async def handle_add_user_command(self, command: RegisterUserCommandDTO) -> RegisterUserResultDTO:
        ...

    async def handle_remove_user_command(self, command: RemoveUserCommandDTO) -> None:
        ...
