from fastapi import APIRouter, Depends

from constants import API_PREFIX

from .controllers import users, auth, bin, products, recipes, dictionaries

authorized_router = APIRouter(dependencies=[Depends(auth.check_access_token), Depends(auth.check_csrf_token)])
authorized_router.include_router(users.router)
authorized_router.include_router(bin.router)
authorized_router.include_router(products.router)
authorized_router.include_router(recipes.router)
authorized_router.include_router(dictionaries.router)

api_router = APIRouter(prefix=f"{API_PREFIX}", dependencies=[Depends(auth.issue_csrf_token)])
api_router.include_router(auth.router)
api_router.include_router(authorized_router)
