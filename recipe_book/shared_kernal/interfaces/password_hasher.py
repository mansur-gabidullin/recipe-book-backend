from typing import Protocol, runtime_checkable


@runtime_checkable
class IPasswordHasher(Protocol):
    async def hash(self, password: str) -> str:
        ...

    async def verify(self, hash_: str, password: str) -> bool:
        ...
