from importlib.metadata import metadata
from typing import Literal

from pydantic import BaseSettings

recipe_book_metadata = metadata("recipe-book-backend")


class Settings(BaseSettings):
    env_mode: Literal["development", "production", "testing"] = "development"
    dev_frontend_origin: str
    server_host: str
    server_port: int
    db_name: str
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    token_algorithm: str
    token_secret_key: str
    csrf_token_expire_minutes: int
    access_token_expire_minutes: int
    refresh_token_expire_days: int
    refresh_token_cookie_key: str


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
