from unittest.mock import Mock, AsyncMock, patch, call

import pytest


@pytest.mark.asyncio
@patch("dataclasses.asdict", lambda o: {"id": 1, "login": "test"})
async def test_users_query_handler():
    from application_core.bounded_contexts.users.use_cases.admin import UsersAdminUseCase

    repository = AsyncMock()
    repository.get_users = AsyncMock()
    user_entity = Mock()
    repository.get_users.return_value = [user_entity]
    query_dto = Mock()
    use_case = UsersAdminUseCase(repository)

    await use_case.handle_users_query(query_dto)

    repository.get_users.assert_called()
    repository.get_users.assert_awaited()
    repository.get_users.assert_has_calls([call(query_dto)])
