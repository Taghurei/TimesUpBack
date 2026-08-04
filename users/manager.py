from core.manager import MongoManager
from users.model import User


class UserManager(MongoManager):
    def __init__(self):
        super().__init__("users")

    def get_all(self):
        return [User.from_dict(x) for x in super().get_all()]

    def get(self, user_id):
        user = super().get(user_id)
        return User.from_dict(user) if user else None

    def get_by_nickname(self, nickname):
        user = super().get_one({"nickname": nickname})
        return User.from_dict(user) if user else None

    def insert_one(self, user):
        return super().insert_one(user.to_insert_dict())

    def update_one(self, user):
        return super().update_one(user.user_id, user.to_update_dict())
