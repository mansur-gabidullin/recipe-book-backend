from dataclasses import dataclass

from ...interfaces.auth.access_token_response_model import IAccessTokenResponseModel


@dataclass
class AccessTokenResponseModel(IAccessTokenResponseModel):
    access_token: str
    token_type: str
