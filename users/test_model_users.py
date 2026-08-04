import pytest

from users.model import User
from users.test_model_data_users import correct_users_data, incorrect_users_data


def get_user(test_input):
    return User(
        _id=test_input["_id"],
        created_at=test_input["created_at"],
        updated_at=test_input["updated_at"],
        nickname=test_input["nickname"],
        password_hash=test_input["password_hash"],
    )


class TestInit:
    @pytest.mark.parametrize("test_input,expected", correct_users_data)
    def test_user_legit_args(self, test_input, expected):
        user = get_user(test_input)

        assert user._id == expected["_id"]
        assert user.user_id == expected["user_id"]
        assert user.created_at == expected["created_at"]
        assert user.updated_at == expected["updated_at"]
        assert user.nickname == expected["nickname"]
        assert user.password_hash == expected["password_hash"]

    @pytest.mark.parametrize("test_input,error_raised", incorrect_users_data)
    def test_error(self, test_input, error_raised):
        with pytest.raises(error_raised):
            user = get_user(test_input)


class TestExport:
    @pytest.mark.parametrize("test_input,expected", correct_users_data)
    def test_password_hash_never_leaves_the_back(self, test_input, expected):
        user = get_user(test_input)

        assert "password_hash" not in user.to_dict()
        assert user.to_dict() == {
            "user_id": expected["user_id"],
            "nickname": expected["nickname"],
        }

    @pytest.mark.parametrize("test_input,expected", correct_users_data)
    def test_password_hash_is_stored(self, test_input, expected):
        user = get_user(test_input)

        assert user.to_insert_dict()["password_hash"] == expected["password_hash"]

    @pytest.mark.parametrize("test_input,expected", correct_users_data)
    def test_from_dict_reads_a_stored_user(self, test_input, expected):
        user = User.from_dict(get_user(test_input).to_insert_dict())

        assert user.user_id == expected["user_id"]
        assert user.nickname == expected["nickname"]
        assert user.password_hash == expected["password_hash"]
