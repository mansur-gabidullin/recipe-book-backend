from fastapi import APIRouter, Depends

from .controllers import users, admin_panel, recipe_book, auth
from .controllers.auth import check_user_authorization

api_router = APIRouter(prefix="/api")
api_router.include_router(auth.router)
api_router.include_router(users.router, dependencies=[Depends(check_user_authorization)])
api_router.include_router(admin_panel.router, dependencies=[Depends(check_user_authorization)])
api_router.include_router(recipe_book.router)
