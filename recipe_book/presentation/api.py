from fastapi import APIRouter, Depends

from .controllers import users, auth, bin, products, recipes
from .controllers.auth import check_user_authorization, create_csrf_token, check_csrf_token

authorized_router = APIRouter(dependencies=[Depends(check_user_authorization), Depends(check_csrf_token)])
authorized_router.include_router(users.router)
authorized_router.include_router(bin.router)
authorized_router.include_router(products.router)
authorized_router.include_router(recipes.router)

api_router = APIRouter(prefix="/api", dependencies=[Depends(create_csrf_token)])
api_router.include_router(auth.router)
api_router.include_router(authorized_router)
