import contextlib
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from infrastructure.session import AsyncScopedSession
from settings import recipe_book_metadata, settings

from .api import api_router

tags_metadata = []


@contextlib.asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    yield
    await AsyncScopedSession.remove()


app = FastAPI(
    title=recipe_book_metadata["Name"],
    description=recipe_book_metadata["Description"],
    version=recipe_book_metadata["Version"],
    openapi_tags=tags_metadata,
)

app.include_router(api_router)

if settings.env_mode == "development":
    origins = [settings.dev_frontend_origin]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
