import uvicorn

from shared_kernel.create_env import run as run_create_env
from shared_kernel.init_db import run as run_init_db
from shared_kernel.settings import settings


def create_env():
    run_create_env()


def init_db():
    run_init_db()


def run():
    uvicorn.run(
        'src.user_interface.framework_fastapi:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )


if __name__ == '__main__':
    run()
