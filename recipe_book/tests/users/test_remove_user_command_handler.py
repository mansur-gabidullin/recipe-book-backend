from unittest.mock import Mock, AsyncMock
from uuid import uuid4

import pytest

from application_core.users.services.users import UsersService


@pytest.mark.asyncio
async def test_remove_user_command_handler():
    fake_uuid = uuid4()
    command_dto = Mock(uuid=fake_uuid)
    command_dto.dict = Mock(return_value={"uuid": fake_uuid})

    def mock_remove_user(uuid):
        return fake_uuid == uuid

    repository = AsyncMock()
    repository.remove_user = AsyncMock(side_effect=mock_remove_user)

    password_hasher = Mock()
    converter = Mock()

    use_case = UsersService(repository, converter, password_hasher)

    await use_case.remove_user(command_dto)

    repository.remove_user.assert_awaited_once()
