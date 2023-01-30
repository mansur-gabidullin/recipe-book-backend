from fastapi import APIRouter

from .routes import users, admin_panel, recipe_book

api_router = APIRouter(prefix='/api')
api_router.include_router(users.router)
api_router.include_router(admin_panel.router)
api_router.include_router(recipe_book.router)
