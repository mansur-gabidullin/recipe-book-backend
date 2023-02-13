from unittest.mock import Mock, AsyncMock
from uuid import uuid4

import pytest

from application_core.bounded_contexts.users.use_cases.admin import UsersAdminUseCase


@pytest.mark.asyncio
async def test_add_user_command_handler():
    password = "fake_password"
    data = {"login": "test", "password": password, "password_confirm": password, "email": "test@test.com"}
    command_dto = Mock(**data)
    command_dto.configure_mock(password=password)
    command_dto.dict = Mock(return_value=data)
    fake_uuid = uuid4()

    def mock_add_user(po):
        assert po.login == command_dto.login
        assert po.email == command_dto.email
        return fake_uuid

    repository = AsyncMock()
    repository.add_user = AsyncMock(side_effect=mock_add_user)

    def hash_(password_):
        assert password_ == password
        return password_

    password_hasher = AsyncMock
    password_hasher.hash = AsyncMock(side_effect=hash_)

    use_case = UsersAdminUseCase(repository, password_hasher)

    await use_case.handle_add_user_command(command_dto)

    repository.add_user.assert_awaited_once()
