from ..beans.profile_record import ProfileRecord
from ..beans.user_record import UserRecord
from ..helpers import scalar_as_dict
from ..interfaces.user_repository_converter import IUserRepositoryConverter


class UserRepositoryConverter(IUserRepositoryConverter):
    def from_query_results(self, results):
        users = []

        for item in results.mappings():
            profile = ProfileRecord(**scalar_as_dict(item.Profiles)) if item.Profiles else None
            users.append(UserRecord(**scalar_as_dict(item.Users), profile=profile))

        return users
