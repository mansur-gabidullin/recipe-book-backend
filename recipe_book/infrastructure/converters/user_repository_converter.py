from ..beans.profile_result import ProfileResult
from ..beans.user_result import UserRecord
from ..helpers import scalar_as_dict
from ..interfaces.user_repository_converter import IUserRepositoryConverter


class UserRepositoryConverter(IUserRepositoryConverter):
    def from_users_results(self, results):
        users = []

        for item in results.mappings():
            profile = ProfileResult(**scalar_as_dict(item.Profiles)) if item.Profiles else None
            users.append(UserRecord(**scalar_as_dict(item.Users), profile=profile))

        return users
