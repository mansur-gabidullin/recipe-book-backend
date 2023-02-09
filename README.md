# recipe-book-backend

A backend for web app for cooking recipes.

## commands to run from scratch
+ install docker (https://docs.docker.com/engine/install/)
+ launch docker
+ install pyenv (https://github.com/pyenv/pyenv#installation)
+ install python `pyenv install 3.11`
+ enable python version, e.g. `pyenv global 3.11` (https://github.com/pyenv/pyenv#switch-between-python-versions)
+ install poetry (https://python-poetry.org/docs/#installation)
+ clone project to your machine
+ open project folder in terminal
+ bootstrap PostgresQL in docker by running `.docker/start.sh`
+ install project dependencies `poetry install --only prod`
+ create .env file for environment variables `poetry run create_env`
+ create tables in PostgresQL database `poetry run init_db`
+ run dev-server `poetry run start`
+ open http://0.0.0.0:9000/docs for API documentation

## other commands
+ install all dependencies `poetry install`
+ run tests `pytest`
+ open htmlcov/index.html to view coverage
+ run code formatter `black recipe_book`
+ run static type checker `mypy`
+ run static code analyser `pylint recipe_book`
+ run the pre-commit hooks against all of the files `pre-commit run --all-files`

## technology stack
+ Python 3.11
+ Poetry
+ Pydantic
+ FastAPI
+ SQLAlchemy
+ Uvicorn
+ PostgresQL

### Todo

#### admin-panel
- [ ] super-user
- [ ] Logging
- [ ] Authentication by login/password
- [ ] OAuth2.0
- [ ] Sending emails
- [ ] Permissions
- [ ] Database migrations
#### Recipe book
- [ ] Photo storage
- [ ] Parser
- [ ] Telegram bot
#### Monitoring
- [ ] Collection of logs
- [ ] Draw graphs
- [ ] Send error notifications
#### Frontend ([repo](https://github.com/mansur-gabidullin/recipe-book-frontend))
- [ ] Captcha
- [ ] SSR
- [ ] Csrf-token
#### Testing
- [ ] unit-tests
- [ ] API tests
- [ ] Integration
- [ ] E2E
#### Docker
- [ ] Dockerize everything
