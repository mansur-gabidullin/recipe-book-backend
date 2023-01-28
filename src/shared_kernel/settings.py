from importlib.metadata import metadata

from pydantic import BaseSettings

recipe_book_metadata = metadata("recipe-book-backend")


class Settings(BaseSettings):
    server_host: str = '0.0.0.0'
    server_port: int = 9000
    db_name: str
    db_host: str
    db_port: str
    db_user: str
    db_password: str


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
