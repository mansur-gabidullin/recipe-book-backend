from typing import Protocol, runtime_checkable


@runtime_checkable
class IAccessTokenResponseModel(Protocol):
    access_token: str
    token_type: str
