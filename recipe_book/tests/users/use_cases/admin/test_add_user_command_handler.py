from unittest.mock import Mock, AsyncMock

import pytest

from application_core.bounded_contexts.users.use_cases.admin import UsersAdminUseCase


@pytest.mark.asyncio
async def test_add_user_command_handler():
    data = {"login": "test", "email": "test@test.test"}
    command_dto = Mock(**data)
    command_dto.dict = Mock(return_value=data)

    def mock_add_user(po):
        assert po.login == command_dto.login
        assert po.email == command_dto.email
        return 1

    repository = AsyncMock()
    repository.add_user = AsyncMock()
    repository.add_user.side_effect = mock_add_user
    use_case = UsersAdminUseCase(repository)

    await use_case.handle_add_user_command(command_dto)

    repository.add_user.assert_called_once()
    repository.add_user.assert_awaited()
