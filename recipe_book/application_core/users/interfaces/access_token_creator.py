from typing import Protocol, runtime_checkable


@runtime_checkable
class IAccessTokenCreator(Protocol):
    async def create(self, data: dict) -> str:
        ...

    async def read(self, token: str) -> dict:
        ...
