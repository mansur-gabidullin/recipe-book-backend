from dataclasses import dataclass
from unittest.mock import Mock, AsyncMock, call
from uuid import UUID, uuid4

import pytest

from application_core.users.services.users import UsersService


@pytest.mark.asyncio
async def test_users_query_handler():
    @dataclass
    class UserEntityMock:
        uuid: UUID = uuid4()
        login: str = "test"
        password_hash: str = "fake password"
        is_removed: bool = False
        is_active: bool = False

    repository = AsyncMock()
    user_entity = UserEntityMock()
    repository.get_users = AsyncMock(return_value=[user_entity])

    query_dto = Mock()
    password_hasher = Mock()
    converter = Mock()

    use_case = UsersService(repository, converter, password_hasher)
    await use_case.get_users_list(query_dto)

    repository.get_users.assert_awaited_once()
    repository.get_users.assert_has_calls([call(query_dto)])
