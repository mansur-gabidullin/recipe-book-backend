from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from application_core.bounded_contexts.users.beans.token_dto import Token
from application_core.bounded_contexts.users.ports.secondary import IAccessTokenCreator

from ..dependencies import authenticate_user, access_token_creator_factory
from ..exceptions import credentials_exception

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token", response_model=Token, dependencies=[Depends(authenticate_user)])
async def endpoint_for_getting_authentication_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    token_creator: IAccessTokenCreator = Depends(access_token_creator_factory),
):
    try:
        return {"access_token": await token_creator.create(data={"sub": form_data.username}), "token_type": "bearer"}
    except Exception:
        raise credentials_exception
