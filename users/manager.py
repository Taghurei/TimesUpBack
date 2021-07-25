from core.manager import MongoManager
from users.model import User


class UserManager(MongoManager):
    def __init__(self):
        super().__init__("users")

    def get(self, user_id):
        return User.from_dict(self.collection.find_one({"_id": user_id}))

    def get_one_by_query(self, query):
        result = self.collection.find_one(query)
        return User.from_dict(result) if result else None

    def get_all(self):
        return [User.from_dict(x) for x in super().get_all()]

    def insert_one(self, user):
        return super().insert_one(user.to_insert_dict())

    def update_one(self, user):
        return super().update_one({"_id": user.user_id}, user.to_insert_dict())