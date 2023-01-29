def run():
    from src.settings import settings
    from uvicorn import run

    run(
        'src.presentation.framework_fastapi.app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
