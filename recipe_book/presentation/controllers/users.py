from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException
from starlette.responses import Response
from starlette.status import HTTP_400_BAD_REQUEST

from dependencies import (
    create_users_service,
    create_users_query,
    create_user_request_converter,
    create_add_user_command,
    create_remove_user_command,
)

from application_core.users.interfaces.add_user_command import IAddUserCommand
from application_core.users.interfaces.remove_user_command import IRemoveUserCommand
from application_core.users.interfaces.user_entity import IUserEntity
from application_core.users.interfaces.users_query import IUsersQuery
from application_core.users.interfaces.users_service import IUsersService

from ..interfaces.new_user_response_model import INewUserResponseModel
from ..interfaces.user_response_model import IUserResponseModel
from ..interfaces.user_converter import IUserResponseConverter

from ..beans.new_user_response_model import NewUserResponseModel
from ..beans.user_response_model import UserResponseModel

from .auth import get_current_active_user

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
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Incorrect data")
    return users_converter.from_new_user(user)


@router.delete("/{uuid}", status_code=204, response_class=Response)
async def delete_user(
    remove_user_command: IRemoveUserCommand = Depends(create_remove_user_command),
    users_service: IUsersService = Depends(create_users_service),
) -> None:
    return await users_service.remove_user(remove_user_command)


@router.get("/profile", response_model=UserResponseModel)
async def get_current_user(
    user: IUserEntity | None = Depends(get_current_active_user),
    users_converter: IUserResponseConverter = Depends(create_user_request_converter),
) -> IUserResponseModel | None:
    return users_converter.from_users([user])[0] if user else None
