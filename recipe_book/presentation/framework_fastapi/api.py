from fastapi import APIRouter, Depends

from .dependencies import oauth2_scheme
from .routes import users, admin_panel, recipe_book, auth

api_router = APIRouter(prefix="/api")
api_router.include_router(auth.router)
api_router.include_router(users.router, dependencies=[Depends(oauth2_scheme)])
api_router.include_router(admin_panel.router, dependencies=[Depends(oauth2_scheme)])
api_router.include_router(recipe_book.router)
