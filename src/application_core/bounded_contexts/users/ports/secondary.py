from typing import Protocol

from ..beans.add_user_result_dto import AddUserResultDTO
from ..beans.user_dto import UserDTO
from ..beans.user_po import UserPO
from ..beans.users_query_dto import UsersQueryDTO


class IUsersRepository(Protocol):
    async def get_users(self, query: UsersQueryDTO) -> list[UserDTO]:
        ...

    async def add_user(self, user: UserPO) -> AddUserResultDTO:
        ...
