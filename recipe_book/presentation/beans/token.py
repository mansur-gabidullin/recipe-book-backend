from pydantic import BaseModel


class Token(BaseModel):  # implements IToken
    access_token: str
    token_type: str
