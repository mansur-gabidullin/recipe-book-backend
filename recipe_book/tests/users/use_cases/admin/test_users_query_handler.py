from dataclasses import dataclass
from unittest.mock import Mock, AsyncMock, call
from uuid import UUID

import pytest

from application_core.bounded_contexts.users.use_cases.admin import UsersAdminUseCase


@pytest.mark.asyncio
async def test_users_query_handler():
    repository = AsyncMock()
    repository.get_users = AsyncMock()

    @dataclass
    class UserEntityMock:
        uuid: UUID = 1
        login: str = "test"

    user_entity = UserEntityMock()
    repository.get_users.return_value = [user_entity]

    query_dto = Mock()

    use_case = UsersAdminUseCase(repository)
    await use_case.handle_users_query(query_dto)

    repository.get_users.assert_called()
    repository.get_users.assert_awaited()
    repository.get_users.assert_has_calls([call(query_dto)])
