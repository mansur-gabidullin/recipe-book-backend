from sqlalchemy import Result

from .beans.profile_result import ProfileResult
from .beans.user_result import UserResult
from .helpers import scalar_as_dict
from .interfaces.users_converter import IUsersInfrastructureConverter


class UsersInfrastructureConverter(IUsersInfrastructureConverter):
    def from_users_results(self, results: Result):
        users = []

        for item in results.mappings():
            profile = ProfileResult(**scalar_as_dict(item.Profiles)) if item.Profiles else None
            users.append(UserResult(**scalar_as_dict(item.Users), profile=profile))

        return users
