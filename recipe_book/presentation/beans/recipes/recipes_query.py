from dataclasses import dataclass

from application_core.recipes.interfaces.recipes_query import IRecipesQuery


@dataclass
class RecipesQuery(IRecipesQuery):
    limit: int | None
    is_removed: bool = False
