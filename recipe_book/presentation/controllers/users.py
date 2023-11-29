from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException
from starlette.responses import Response
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from dependencies import (
    create_users_service,
    create_users_query,
    create_user_request_converter,
    create_add_user_command,
    create_remove_user_command,
    create_auth_service,
)

from application_core.auth.interfaces.access_token import IAccessToken
from application_core.auth.interfaces.auth_service import IAuthService

from application_core.users.interfaces.add_user_command import IAddUserCommand
from application_core.users.interfaces.remove_user_command import IRemoveUserCommand
from application_core.users.interfaces.users_query import IUsersQuery
from application_core.users.interfaces.users_service import IUsersService

from ..interfaces.users.new_user_response_model import INewUserResponseModel
from ..interfaces.users.user_response_model import IUserResponseModel
from ..interfaces.users.user_converter import IUserResponseConverter

from ..beans.users.new_user_response_model import NewUserResponseModel
from ..beans.users.user_response_model import UserResponseModel

from .auth import get_access_token

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserResponseModel])
async def get_users(
    users_query: IUsersQuery = Depends(create_users_query),
    users_converter: IUserResponseConverter = Depends(create_user_request_converter),
    users_service: IUsersService = Depends(create_users_service),
) -> list[IUserResponseModel]:
    users = await users_service.get_users_list(users_query)
    return users_converter.from_users(users)


@router.post("/", response_model=NewUserResponseModel)
async def add_user(
    add_user_command: IAddUserCommand = Depends(create_add_user_command),
    users_converter: IUserResponseConverter = Depends(create_user_request_converter),
    users_service: IUsersService = Depends(create_users_service),
) -> INewUserResponseModel:
    try:
        user = await users_service.add_user(add_user_command)
    # todo: use custom error
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Incorrect data")
    return users_converter.from_new_user(user)


@router.delete("/{uuid}", status_code=HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user(
    remove_user_command: IRemoveUserCommand = Depends(create_remove_user_command),
    users_service: IUsersService = Depends(create_users_service),
) -> None:
    return await users_service.remove_user(remove_user_command)


@router.get("/profile", response_model=UserResponseModel | None)
async def get_current_user(
    access_token: IAccessToken = Depends(get_access_token),
    auth_service: IAuthService = Depends(create_auth_service),
    users_converter: IUserResponseConverter = Depends(create_user_request_converter),
) -> IUserResponseModel | None:
    if not access_token:
        return None

    user = await auth_service.get_current_active_user(access_token)

    return users_converter.from_users([user])[0] if user else None
