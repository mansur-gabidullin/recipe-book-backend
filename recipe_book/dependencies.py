from typing import AsyncIterator
from uuid import UUID

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from settings import settings

from constants import API_PREFIX

from shared_kernal.interfaces.access_token_creator import ITokenCreator
from shared_kernal.interfaces.password_hasher import IPasswordHasher
from shared_kernal.token_creator import TokenCreator
from shared_kernal.password_hasher import PasswordHasher

from application_core.auth.interfaces.auth_service import IAuthService
from application_core.auth.services.auth_service import AuthService

from application_core.bin.interfaces.bin_restore_command import IBinCommand
from application_core.bin.interfaces.bin_action import IBinAction
from application_core.bin.interfaces.bin_repository import IBinRepository
from application_core.bin.interfaces.bin_service import IBinService
from application_core.bin.services.bin_restore_service import BinService

from application_core.products.interfaces.change_product_command import IChangeProductCommand
from application_core.products.interfaces.product_query import IProductQuery
from application_core.products.interfaces.remove_product_command import IRemoveProductCommand
from application_core.products.interfaces.add_product_command import IAddProductCommand
from application_core.products.interfaces.products_query import IProductsQuery
from application_core.products.interfaces.products_repository import IProductsRepository
from application_core.products.interfaces.products_service import IProductsService
from application_core.products.interfaces.products_service_converter import IProductsServiceConverter
from application_core.products.converters.products_service_converter import ProductsServiceConverter
from application_core.products.services.products_service import ProductsService

from application_core.recipes.interfaces.add_recipe_command import IAddRecipeCommand
from application_core.recipes.interfaces.recipes_service_converter import IRecipesServiceConverter
from application_core.recipes.interfaces.recipes_query import IRecipesQuery
from application_core.recipes.interfaces.recipes_repository import IRecipesRepository
from application_core.recipes.interfaces.recipes_service import IRecipesService
from application_core.recipes.converters.recipes_service_converter import RecipesServiceConverter
from application_core.recipes.services.recipes_service import RecipesService

from application_core.users.interfaces.add_user_command import IAddUserCommand
from application_core.users.interfaces.remove_user_command import IRemoveUserCommand
from application_core.users.interfaces.users_service_converter import IUsersServiceConverter
from application_core.users.interfaces.users_query import IUsersQuery
from application_core.users.interfaces.users_repository import IUsersRepository
from application_core.users.interfaces.users_service import IUsersService
from application_core.users.converters.users_service_converter import UsersServiceConverter
from application_core.users.services.users_service import UsersService

from infrastructure.interfaces.product_repository_converter import IProductRepositoryConverter
from infrastructure.interfaces.recipe_repository_converter import IRecipeRepositoryConverter
from infrastructure.interfaces.user_repository_converter import IUserRepositoryConverter
from infrastructure.converters.product_repository_converter import ProductRepositoryConverter
from infrastructure.converters.recipe_repository_converter import RecipeRepositoryConverter
from infrastructure.converters.user_repository_converter import UserRepositoryConverter
from infrastructure.repositories.products_repository import ProductsRepository
from infrastructure.repositories.recipes_repository import RecipesRepository
from infrastructure.repositories.users_repository import UsersRepository
from infrastructure.repositories.users_bin_repository import BinRepository
from infrastructure.session import AsyncScopedSession

from presentation.interfaces.products.product_converter import IProductResponseConverter
from presentation.interfaces.recipes.recipe_converter import IRecipeResponseConverter
from presentation.interfaces.users.user_converter import IUserResponseConverter
from presentation.interfaces.dictionary.dictionary_converter import IDictionaryResponseConverter
from presentation.beans.products.add_product_command import AddProductCommand
from presentation.beans.products.products_query import ProductsQuery
from presentation.beans.recipes.recipes_query import RecipesQuery
from presentation.beans.recipes.add_recipe_command import AddRecipeCommand
from presentation.beans.users.add_user_command import AddUserCommand
from presentation.beans.users.remove_user_command import RemoveUserCommand
from presentation.beans.bin.bin_command import BinCommand
from presentation.beans.users.users_query import UsersQuery
from presentation.beans.products.change_product_command import ChangeProductCommand
from presentation.beans.products.product_query import ProductQuery
from presentation.beans.products.remove_product_command import RemoveProductCommand
from presentation.converters.products_response_converter import ProductResponseConverter
from presentation.converters.recipes_response_converter import RecipeResponseConverter
from presentation.converters.users_response_converter import UserResponseConverter
from presentation.converters.dictionary_response_converter import DictionaryResponseConverter

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{API_PREFIX}/auth/token", auto_error=False)


async def create_database_session() -> AsyncIterator[AsyncSession]:
    async with AsyncScopedSession() as session:
        async with session.begin():
            try:
                yield session
            except Exception as error:
                print(error)
                await session.rollback()
                raise error


async def create_token_creator() -> ITokenCreator:
    return TokenCreator(
        secret_key=settings.token_secret_key,
        algorithm=settings.token_algorithm,
        csrf_expire_minutes=settings.csrf_token_expire_minutes,
        access_expire_minutes=settings.access_token_expire_minutes,
        refresh_expire_days=settings.refresh_token_expire_days,
    )


async def create_password_hasher() -> IPasswordHasher:
    return PasswordHasher()


async def create_users_query(login: str = None, limit: int = None) -> IUsersQuery:
    return UsersQuery(login=login, limit=limit)


async def create_add_user_command(addUserCommand: AddUserCommand) -> IAddUserCommand:
    return addUserCommand


async def create_remove_user_command(uuid: UUID) -> IRemoveUserCommand:
    return RemoveUserCommand(uuid=uuid)


async def create_user_request_converter() -> IUserResponseConverter:
    return UserResponseConverter()


async def create_users_service_converter() -> IUsersServiceConverter:
    return UsersServiceConverter()


async def create_user_repository_converter() -> IUserRepositoryConverter:
    return UserRepositoryConverter()


async def create_users_repository(
    session: AsyncSession = Depends(create_database_session),
    converter: IUserRepositoryConverter = Depends(create_user_repository_converter),
) -> IUsersRepository:
    return UsersRepository(session, converter)


async def create_users_service(
    repository: IUsersRepository = Depends(create_users_repository),
    converter: IUsersServiceConverter = Depends(create_users_service_converter),
    password_hasher: IPasswordHasher = Depends(create_password_hasher),
) -> IUsersService:
    return UsersService(repository, converter, password_hasher)


async def create_auth_service(
    token_creator: ITokenCreator = Depends(create_token_creator),
    user_service: IUsersService = Depends(create_users_service),
    password_hasher: IPasswordHasher = Depends(create_password_hasher),
) -> IAuthService:
    return AuthService(token_creator, user_service, password_hasher)


async def create_bin_restore_repository(
    session: AsyncSession = Depends(create_database_session),
) -> IBinRepository:
    return BinRepository(session)


async def create_bin_restore_service(
    repository: IBinRepository = Depends(create_bin_restore_repository),
) -> IBinService:
    return BinService(repository)


async def create_bin_command(uuid: UUID, action: IBinAction) -> IBinCommand:
    return BinCommand(uuid=uuid, action=action)


async def create_users_bin_query(login: str = None, limit: int = None) -> IUsersQuery:
    return UsersQuery(login=login, limit=limit, is_removed=True)


async def create_recipes_query(limit: int = None) -> IRecipesQuery:
    return RecipesQuery(limit=limit)


async def create_recipes_response_converter() -> IRecipeResponseConverter:
    return RecipeResponseConverter()


async def create_recipe_repository_converter() -> IRecipeRepositoryConverter:
    return RecipeRepositoryConverter()


async def create_recipes_repository(
    session: AsyncSession = Depends(create_database_session),
    repository_converter: IRecipeRepositoryConverter = Depends(create_recipe_repository_converter),
) -> IRecipesRepository:
    return RecipesRepository(session, repository_converter)


async def create_recipes_service_converter() -> IRecipesServiceConverter:
    return RecipesServiceConverter()


async def create_recipes_service(
    repository: IRecipesRepository = Depends(create_recipes_repository),
    service_converter: IRecipesServiceConverter = Depends(create_recipes_service_converter),
) -> IRecipesService:
    return RecipesService(repository, service_converter)


async def create_add_recipe_command(addRecipeCommand: AddRecipeCommand) -> IAddRecipeCommand:
    return addRecipeCommand


async def create_products_query(limit: int = None) -> IProductsQuery:
    return ProductsQuery(limit=limit)


async def create_product_query(uuid: UUID) -> IProductQuery:
    return ProductQuery(uuid=uuid)


async def create_products_response_converter() -> IProductResponseConverter:
    return ProductResponseConverter()


async def create_product_repository_converter() -> IProductRepositoryConverter:
    return ProductRepositoryConverter()


async def create_products_repository(
    session: AsyncSession = Depends(create_database_session),
    repository_converter: IProductRepositoryConverter = Depends(create_product_repository_converter),
) -> IProductsRepository:
    return ProductsRepository(session, repository_converter)


async def create_products_service_converter() -> IProductsServiceConverter:
    return ProductsServiceConverter()


async def create_products_service(
    repository: IProductsRepository = Depends(create_products_repository),
    service_converter: IProductsServiceConverter = Depends(create_products_service_converter),
) -> IProductsService:
    return ProductsService(repository, service_converter)


async def create_add_product_command(command: AddProductCommand) -> IAddProductCommand:
    return command


async def create_change_product_command(command: ChangeProductCommand) -> IChangeProductCommand:
    return command


async def create_remove_product_command(uuid: UUID) -> IRemoveProductCommand:
    return RemoveProductCommand(uuid=uuid)


async def create_dictionary_response_converter() -> IDictionaryResponseConverter:
    return DictionaryResponseConverter()
