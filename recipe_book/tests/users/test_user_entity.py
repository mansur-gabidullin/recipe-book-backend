from uuid import uuid4

from application_core.users.aggregates.user.user_entity import UserEntity


def test_user_entity():
    data = {
        "uuid": uuid4(),
        "login": "login",
        "password_hash": "hash",
        "is_removed": False,
        "is_active": False,
    }

    user_entity = UserEntity(**data)

    assert data.get("uuid") == user_entity.uuid
    assert data.get("login") == user_entity.login
    assert data.get("password_hash") == user_entity.password_hash
