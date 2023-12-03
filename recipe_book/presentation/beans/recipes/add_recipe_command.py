from dataclasses import dataclass
from typing import Annotated

from pydantic import StringConstraints, Field

from application_core.recipes.interfaces.add_recipe_command import IAddRecipeCommand

from constants import (
    RECIPE_TITLE_MIN_LENGTH,
    RECIPE_TITLE_MAX_LENGTH,
    RECIPE_DESCRIPTION_MIN_LENGTH,
    RECIPE_DESCRIPTION_MAX_LENGTH,
    RECIPE_AUTHOR_MIN_LENGTH,
    RECIPE_AUTHOR_MAX_LENGTH,
    RECIPE_IMAGE_URL_MAX_LENGTH,
)

from .add_recipe_command_cooking_step_data import AddRecipeCommandCookingStepData


@dataclass
class AddRecipeCommand(IAddRecipeCommand):
    title: Annotated[
        str,
        StringConstraints(min_length=RECIPE_TITLE_MIN_LENGTH, max_length=RECIPE_TITLE_MAX_LENGTH),
    ]
    description: Annotated[
        str,
        StringConstraints(min_length=RECIPE_DESCRIPTION_MIN_LENGTH, max_length=RECIPE_DESCRIPTION_MAX_LENGTH),
    ]
    number_of_servings: Annotated[int, Field(gt=0)]
    cooking_steps: list[AddRecipeCommandCookingStepData]
    image_url: Annotated[
        str | None,
        StringConstraints(max_length=RECIPE_IMAGE_URL_MAX_LENGTH),
    ] = None
    author: Annotated[
        str | None,
        StringConstraints(min_length=RECIPE_AUTHOR_MIN_LENGTH, max_length=RECIPE_AUTHOR_MAX_LENGTH),
    ] = None
