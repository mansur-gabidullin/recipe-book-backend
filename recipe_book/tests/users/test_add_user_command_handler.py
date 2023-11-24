from unittest.mock import Mock, AsyncMock
from uuid import uuid4

import pytest

from application_core.users.services.users_service import UsersService


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

    converter = Mock()

    def to_user_data(_, password_hash, is_active=True):
        user_data = Mock()
        user_data.configure_mock(**data, password_hash=password_hash, is_active=is_active)
        return user_data

    converter.to_user_data = Mock(side_effect=to_user_data)

    users_service = UsersService(repository, converter, password_hasher)

    await users_service.add_user(command_dto)

    repository.add_user.assert_awaited_once()
