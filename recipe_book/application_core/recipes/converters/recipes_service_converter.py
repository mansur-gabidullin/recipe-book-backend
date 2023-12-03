from ..beans.ingredient_data import IngredientData
from ..interfaces.recipe_data import IRecipeData
from ..interfaces.recipes_service_converter import IRecipesServiceConverter
from ..beans.recipe_data import RecipeData
from ..beans.cooking_step_data import CookingStepData


class RecipesServiceConverter(IRecipesServiceConverter):
    def to_recipe_data(self, data) -> IRecipeData:
        return RecipeData(
            title=data.title,
            description=data.description,
            number_of_servings=data.number_of_servings,
            image_url=data.image_url,
            author=data.author,
            cooking_steps=[
                CookingStepData(
                    description=cooking_step.description,
                    image_url=cooking_step.image_url,
                    ingredients=[
                        IngredientData(
                            product_uuid=ingredient.product_uuid,
                            quantity=ingredient.quantity,
                            unit=ingredient.unit,
                        )
                        for ingredient in cooking_step.ingredients
                    ],
                )
                for cooking_step in data.cooking_steps
            ],
        )
