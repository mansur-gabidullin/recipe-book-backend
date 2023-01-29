def create_env():
    from scripts.create_env import run
    run()


def init_db():
    from scripts.init_db import run
    run()


def start():
    from scripts.start import run
    run()


if __name__ == '__main__':
    start()
