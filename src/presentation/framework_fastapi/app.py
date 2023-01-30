from fastapi import FastAPI, Request, Response

from settings import recipe_book_metadata

from .api import api_router

tags_metadata = []

app = FastAPI(
    title=recipe_book_metadata['Name'],
    description=recipe_book_metadata['Description'],
    version=recipe_book_metadata['Version'],
    openapi_tags=tags_metadata,
)

app.include_router(api_router)


@app.middleware("http")
async def db_session_middleware(
        request: Request,
        call_next,
):
    from infrastructure.database_sqlalchemy.session import AsyncScopedSession, current_session

    response = Response("Internal server error", status_code=500)

    # noinspection PyBroadException
    try:
        await current_session.begin()
        response = await call_next(request)
        await current_session.commit()
    except Exception:
        await current_session.rollback()
    finally:
        await current_session.close()
        await AsyncScopedSession.remove()

    return response
