from dataclasses import dataclass

from application_core.users.interfaces.token import IAccessTokenData


@dataclass
class AccessTokenData(IAccessTokenData):
    access_token: str
    token_type: str
