from importlib.metadata import metadata

from pydantic import BaseSettings

recipe_book_metadata = metadata("recipe-book-backend")


class Settings(BaseSettings):
    server_host: str
    server_port: int
    db_name: str
    db_host: str
    db_port: int
    db_user: str
    db_password: str


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
