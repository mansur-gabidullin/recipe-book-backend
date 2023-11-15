from typing import Protocol, runtime_checkable
from uuid import UUID


@runtime_checkable
class INewUserResponseModel(Protocol):
    uuid: UUID
