from uuid import uuid4

from application_core.bounded_contexts.users.aggregates.user import UserEntity


def test_user_entity():
    data = {"uuid": uuid4(), "login": "login", "password_hash": "hash", "is_removed": False, "profile": None}
    user_entity = UserEntity(**data)

    assert data.get("uuid") == user_entity.uuid
    assert data.get("login") == user_entity.login
    assert data.get("password_hash") == user_entity.password_hash


def test_password_generation():
    hash_ = UserEntity.generate_password_hash("password")
    assert type(hash_) == str
