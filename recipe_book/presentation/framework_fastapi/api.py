from fastapi import APIRouter, Depends

from .dependencies import check_access_token_exists
from .routes import users, admin_panel, recipe_book, auth

api_router = APIRouter(prefix="/api")
api_router.include_router(auth.router)
api_router.include_router(users.router, dependencies=[Depends(check_access_token_exists)])
api_router.include_router(admin_panel.router, dependencies=[Depends(check_access_token_exists)])
api_router.include_router(recipe_book.router)
