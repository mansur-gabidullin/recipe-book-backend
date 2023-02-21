from pydantic import BaseModel


class UsersQuery(BaseModel):  # implements IUsersQuery
    login: str | None
    limit: int | None
