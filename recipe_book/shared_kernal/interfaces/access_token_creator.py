from datetime import timedelta
from typing import Protocol, runtime_checkable


@runtime_checkable
class ITokenCreator(Protocol):
    async def create(self, data: dict, expires_delta: timedelta) -> str:
        ...

    async def create_csrf_token(self, data: dict) -> str:
        ...

    async def create_access_token(self, data: dict) -> str:
        ...

    async def create_refresh_token(self, data: dict) -> str:
        ...

    async def read(self, token: str) -> dict:
        ...
