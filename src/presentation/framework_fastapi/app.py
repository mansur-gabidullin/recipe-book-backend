from fastapi import FastAPI, Request, Response

from settings import recipe_book_metadata
from infrastructure.database_sqlalchemy.session import AsyncScopedSession
from presentation.framework_fastapi.api import api_router

tags_metadata = []

app = FastAPI(
    title=recipe_book_metadata['Name'],
    description=recipe_book_metadata['Description'],
    version=recipe_book_metadata['Version'],
    openapi_tags=tags_metadata,
)

app.include_router(api_router)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)

    # noinspection PyBroadException
    try:
        await AsyncScopedSession.begin()
        response = await call_next(request)
        await AsyncScopedSession.commit()
    except Exception:
        await AsyncScopedSession.rollback()
    finally:
        await AsyncScopedSession.close()
        await AsyncScopedSession.remove()

    return response
