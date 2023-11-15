from fastapi import APIRouter, Depends
from starlette.responses import Response
from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from application_core.bin.interfaces.bin_service import IBinService
from application_core.bin.interfaces.bin_action import IBinAction
from application_core.bin.interfaces.user_restore_command import IUserRestoreCommand
from application_core.users.interfaces.users_query import IUsersQuery
from application_core.users.interfaces.users_service import IUsersService

from dependencies import (
    create_users_bin_service,
    create_user_restore_command,
    create_users_bin_query,
    create_user_request_converter,
    create_users_service,
)

from ..constants import BinActionEnum
from ..beans.user_response_model import UserResponseModel

from .users import get_users
from ..interfaces.user_converter import IUserResponseConverter

router = APIRouter(prefix="/bin", tags=["bin"])


@router.get("/users", response_model=list[UserResponseModel])
async def get_users_bin(
    users_query: IUsersQuery = Depends(create_users_bin_query),
    users_converter: IUserResponseConverter = Depends(create_user_request_converter),
    users_service: IUsersService = Depends(create_users_service),
):
    return await get_users(users_query, users_converter, users_service)


@router.put("/{uuid}", status_code=204, response_class=Response)
async def restore_user(
    action: IBinAction,
    restore_command: IUserRestoreCommand = Depends(create_user_restore_command),
    bin_service: IBinService = Depends(create_users_bin_service),
) -> None:
    match action:
        case BinActionEnum.RESTORE:
            return await bin_service.restore(restore_command)
        case _:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f"action {action} is unsupported")
