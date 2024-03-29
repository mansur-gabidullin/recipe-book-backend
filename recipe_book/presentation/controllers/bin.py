from fastapi import APIRouter, Depends
from starlette.responses import Response
from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from application_core.bin.interfaces.bin_service import IBinService
from application_core.bin.interfaces.bin_restore_command import IBinCommand
from application_core.users.interfaces.users_query import IUsersQuery
from application_core.users.interfaces.users_service import IUsersService

from constants import BinActionEnum

from dependencies import (
    create_bin_restore_service,
    create_bin_command,
    create_users_bin_query,
    create_user_request_converter,
    create_users_service,
)

from ..interfaces.users.user_converter import IUserResponseConverter
from ..interfaces.users.user_response_model import IUserResponseModel

from ..beans.users.user_response_model import UserResponseModel

from .users import get_users

router = APIRouter(prefix="/bin", tags=["bin"])


@router.get("", response_model=list[UserResponseModel])
async def get_bin(
    query: IUsersQuery = Depends(create_users_bin_query),
    users_converter: IUserResponseConverter = Depends(create_user_request_converter),
    users_service: IUsersService = Depends(create_users_service),
) -> list[IUserResponseModel]:
    return await get_users(query, users_converter, users_service)


@router.put("/{uuid}", status_code=HTTP_204_NO_CONTENT, response_class=Response)
async def restore(
    command: IBinCommand = Depends(create_bin_command),
    bin_service: IBinService = Depends(create_bin_restore_service),
) -> None:
    match command.action:
        case BinActionEnum.RESTORE:
            return await bin_service.restore(command)
        case _:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f"action {command.action} is unsupported")
