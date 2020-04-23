import time

import pytest

from core.model import Document
from core.test_data import data_init, data_error_args
from core.exceptions import TimesUpDateException


class TestInit:
    def test_default_init(self):
        t_before = int(time.time())
        document = Document()
        t_after = int(time.time())

        # assert _id is not undefined
        assert document._id

        assert document.created_at
        assert document.created_at >= t_before
        assert document.created_at <= t_after

        assert document.updated_at
        assert document.updated_at >= t_before
        assert document.updated_at <= t_after

    @pytest.mark.parametrize("test_input,expected", data_init)
    def test_init(self, test_input, expected):
        document = Document(
            _id=test_input["_id"],
            created_at=test_input["created_at"],
            updated_at=test_input["updated_at"],
        )

        assert document._id == expected["_id"]
        assert document.created_at == expected["created_at"]
        assert document.updated_at == expected["updated_at"]

    @pytest.mark.parametrize("test_input", data_error_args)
    def test_error_args(self, test_input):
        with pytest.raises(TimesUpDateException):
            document = Document(
                _id=test_input["_id"],
                created_at=test_input["created_at"],
                updated_at=test_input["updated_at"],
            )
