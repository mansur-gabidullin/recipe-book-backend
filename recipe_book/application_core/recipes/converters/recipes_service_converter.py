from ..interfaces.recipe_data import IRecipeData
from ..interfaces.recipes_service_converter import IRecipesServiceConverter
from ..beans.recipe_data import RecipeData


class RecipesServiceConverter(IRecipesServiceConverter):
    def to_recipe_data(self, data) -> IRecipeData:
        return RecipeData(
            title=data.title,
            description=data.description,
            number_of_servings=data.number_of_servings,
            cooking_steps=data.cooking_steps,
            image_url=data.image_url,
            author=data.author,
        )
