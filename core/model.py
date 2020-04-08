import time
from uuid import uuid4

class Document:
    fields = [
        "_id",
        "created_at",
        "updated_at",
    ]

    export_fields = [
    ]

    editable_fields = []

    def __init__(
        self, _id: str = None, created_at: int = None, updated_at: int = None,
    ):
        self._id = _id if (_id and isinstance(_id, str)) else str(uuid4())
        self.created_at = created_at if isinstance(created_at, int) else int(time.time())
        self.updated_at = updated_at if isinstance(updated_at, int) else int(time.time())


    def to_dict(self):
        return {key: getattr(self, key) for key in self.export_fields}

    def to_insert_dict(self):
        return {key: getattr(self, key) for key in self.fields}

    def to_update_dict(self):
        return {key: getattr(self, key) for key in self.editable_fields}

    def update(self, inputs: dict = None):
        inputs_filtered = {k: inputs[k] for k in inputs if k in self.editable_fields}
        for key in inputs_filtered:
            setattr(self, key, inputs_filtered[key])
        setattr(self, "updated_at", int(time.time()))


    @staticmethod
    def from_dict(dict_object: dict):
        raise NotImplementedError

    @staticmethod
    def from_dict_class(dict_object: dict, Class):
        kwargs = {
            key: value for (key, value) in dict_object.items() if key in Class.fields
        }
        return Class(**kwargs)
