from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from settings import recipe_book_metadata, settings
from .api import api_router

tags_metadata = []

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


@app.middleware("http")
async def db_session_middleware(
    request: Request,
    call_next,
):
    from infrastructure.database_sqlalchemy.session import current_session, AsyncScopedSession

    response = Response("Internal server error", status_code=500)

    # noinspection PyBroadException
    try:
        await current_session.begin()
        response = await call_next(request)
        await current_session.commit()
    except Exception as error:
        print(error)
        # todo: validation errors to response
        await current_session.rollback()
    finally:
        await current_session.close()
        await AsyncScopedSession.remove()

    return response
