from fastapi import APIRouter, Depends

from dependencies import (
    get_current_active_user,
    create_users_service,
    create_users_query,
    create_users_converter,
    create_add_user_command,
    create_remove_user_command,
)

from application_core.users.interfaces.add_user_command import IAddUserCommand
from application_core.users.interfaces.remove_user_command import IRemoveUserCommand
from application_core.users.interfaces.user import IUser
from application_core.users.interfaces.users_query import IUsersQuery
from application_core.users.interfaces.users_service import IUsersService

from ..interfaces.new_user_response import INewUserResponse
from ..interfaces.user_response import IUserResponse
from ..interfaces.users_converter import IUsersConverter
from ..interfaces.users_list_response import IUsersListResponse
from ..beans.new_user_response import NewUserResponse
from ..beans.user_response import UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserResponse])
async def get_users(
    users_query: IUsersQuery = Depends(create_users_query),
    users_converter: IUsersConverter = Depends(create_users_converter),
    users_service: IUsersService = Depends(create_users_service),
) -> IUsersListResponse:
    users = await users_service.get_users_list(users_query)
    return users_converter.from_users(users)


@router.post("/", response_model=NewUserResponse)
async def add_user(
    add_user_command: IAddUserCommand = Depends(create_add_user_command),
    users_converter: IUsersConverter = Depends(create_users_converter),
    users_service: IUsersService = Depends(create_users_service),
) -> INewUserResponse:
    user = await users_service.add_user(add_user_command)
    return users_converter.from_new_user(user)


@router.delete("/{uuid}")
async def delete_user(
    remove_user_command: IRemoveUserCommand = Depends(create_remove_user_command),
    users_service: IUsersService = Depends(create_users_service),
) -> None:
    return await users_service.remove_user(remove_user_command)


@router.get("/profile", response_model=UserResponse)
async def get_current_user(
    user: IUser = Depends(get_current_active_user),
    users_converter: IUsersConverter = Depends(create_users_converter),
) -> IUserResponse:
    [user] = users_converter.from_users([user])
    return user
