from unittest.mock import Mock, AsyncMock
from uuid import uuid4

import pytest

from application_core.bounded_contexts.users.use_cases.guest import UsersGuestUseCase


@pytest.mark.asyncio
async def test_guest_can_register():
    password = "fake_password"
    data = {"login": "test", "password": password, "password_confirm": password, "email": "test@test.com"}
    register_command = Mock(**data)
    register_command.dict = Mock(return_value=data)
    register_command.configure_mock(password=password)
    fake_uuid = uuid4()

    def mock_register(po):
        assert po.login == data["login"]
        return fake_uuid

    users_repository = Mock()
    users_repository.add_user = AsyncMock(side_effect=mock_register)

    def hash_(password_):
        assert password_ == password
        return password_

    password_hasher = AsyncMock
    password_hasher.hash = AsyncMock(side_effect=hash_)

    guest_use_case = UsersGuestUseCase(users_repository, password_hasher)

    await guest_use_case.handle_register_command(register_command)

    users_repository.add_user.assert_awaited_once()
