from unittest.mock import Mock, AsyncMock
from uuid import uuid4

import pytest

from application_core.bounded_contexts.users.use_cases.guest import UsersGuestUseCase


@pytest.mark.asyncio
async def test_guest_can_register():
    data = {"login": "test"}
    register_command = Mock(**data)
    register_command.dict = Mock(return_value=data)
    fake_uuid = uuid4()

    def mock_register(po):
        assert po.login == data["login"]
        return fake_uuid

    users_repository = Mock()
    users_repository.register_user = AsyncMock(side_effect=mock_register)

    guest_use_case = UsersGuestUseCase(users_repository)

    await guest_use_case.handle_register_command(register_command)

    users_repository.register_user.assert_awaited_once()
