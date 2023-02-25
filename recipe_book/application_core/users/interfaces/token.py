from typing import Protocol, runtime_checkable


@runtime_checkable
class IAccessTokenData(Protocol):
    access_token: str
    token_type: str
