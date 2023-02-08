from application_core.bounded_contexts.users.entities.user import UserEntity


def test_user_entity():
    data = {"id": 1, "login": "login", "password_hash": "hash", "password_solt": "solt", "email": None}

    email = "test@email.ru"

    user_entity = UserEntity(**data)

    assert data.get("id") == user_entity.id
    assert data.get("login") == user_entity.login
    assert data.get("password_hash") == user_entity.password_hash
    assert data.get("password_solt") == user_entity.password_solt
    assert data.get("email") == user_entity.email
    user_entity.email = email
    assert email == user_entity.email


def test_password_generation():
    solt, hash_ = UserEntity.generate_password()
    assert type(solt) == str
    assert type(hash_) == str
