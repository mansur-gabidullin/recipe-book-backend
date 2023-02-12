from unittest.mock import Mock, AsyncMock
from uuid import uuid4

import pytest

from application_core.bounded_contexts.users.use_cases.admin import UsersAdminUseCase


@pytest.mark.asyncio
async def test_remove_user_command_handler():
    fake_uuid = uuid4()
    command_dto = Mock(uuid=fake_uuid)
    command_dto.dict = Mock(return_value={"uuid": fake_uuid})

    def mock_remove_user(uuid):
        return fake_uuid == uuid

    repository = AsyncMock()
    repository.remove_user = AsyncMock(side_effect=mock_remove_user)
    use_case = UsersAdminUseCase(repository)

    await use_case.handle_remove_user_command(command_dto)

    repository.remove_user.assert_awaited_once()
