from uuid import UUID

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from application_core.recipes.interfaces.recipe_entity import IRecipeEntity
from application_core.recipes.interfaces.recipes_repository import IRecipesRepository

from ..interfaces.recipe_repository_converter import IRecipeRepositoryConverter

from ..tables.recipes.cooking_steps import CookingSteps
from ..tables.recipes.ingredients import Ingredients
from ..tables.recipes.recipes import Recipes


class RecipesRepository(IRecipesRepository):
    def __init__(
        self,
        session: AsyncSession,
        converter: IRecipeRepositoryConverter,
    ):
        self._session = session
        self._converter = converter

    async def get_recipes(self, data) -> list[IRecipeEntity]:
        return []

    async def add_recipe(self, data) -> UUID:
        statement = (
            insert(Recipes)
            .values(
                {
                    Recipes.title.key: data.title,
                    Recipes.description.key: data.description,
                    Recipes.number_of_servings.key: data.number_of_servings,
                    Recipes.image_url.key: data.image_url,
                    Recipes.author.key: data.author,
                }
            )
            .returning(Recipes.uuid)
        )

        [recipe_uuid] = (await self._session.execute(statement)).one()

        statement = (
            insert(CookingSteps)
            .values(
                [
                    {
                        CookingSteps.recipe_uuid.key: recipe_uuid,
                        CookingSteps.description.key: step.description,
                        CookingSteps.image_url.key: step.image_url,
                    }
                    for step in data.cooking_steps
                ]
            )
            .returning(CookingSteps.uuid)
        )

        steps_uuids = (await self._session.execute(statement)).scalars().all()

        statement = insert(Ingredients).values(
            [
                {
                    Ingredients.cooking_step_uuid.key: steps_uuids[i],
                    Ingredients.product_uuid.key: ingredient.product_uuid,
                    Ingredients.quantity.key: ingredient.quantity,
                    Ingredients.unit.key: ingredient.unit,
                }
                for i in range(len(data.cooking_steps))
                for ingredient in data.cooking_steps[i].ingredients
            ]
        )

        await self._session.execute(statement)

        return recipe_uuid
