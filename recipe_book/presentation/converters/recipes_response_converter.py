from ..beans.recipes.new_recipe_response_model import NewRecipeResponseModel
from ..interfaces.recipes.recipe_converter import IRecipeResponseConverter


class RecipeResponseConverter(IRecipeResponseConverter):
    def from_recipes(self, recipes):
        # todo
        return []

    def from_new_recipe(self, uuid):
        return NewRecipeResponseModel(uuid=uuid)
