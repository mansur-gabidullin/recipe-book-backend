from fastapi import APIRouter, Depends

from application_core.bounded_contexts.users.beans.token_dto import Token

from ..dependencies import authenticate_user, access_token_factory

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token", response_model=Token, dependencies=[Depends(authenticate_user)])
async def endpoint_for_getting_authentication_token(access_token_data: Token = Depends(access_token_factory)):
    return access_token_data
