from fastapi import APIRouter, Depends

from dependencies import authenticate_user, create_access_token

from application_core.users.interfaces.token import IToken

from ..beans.token import Token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token", response_model=Token, dependencies=[Depends(authenticate_user)])
async def generate_token(access_token_data: IToken = Depends(create_access_token)) -> IToken:
    return access_token_data
