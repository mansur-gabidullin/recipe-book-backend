from dataclasses import dataclass

from application_core.users.interfaces.token import IToken


@dataclass
class Token(IToken):
    access_token: str
    token_type: str
