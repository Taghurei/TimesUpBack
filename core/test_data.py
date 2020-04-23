data_init = [
    (
        # Good type but not realistic data
        {"_id": "a", "created_at": 0, "updated_at": 0},
        {"_id": "a", "created_at": 0, "updated_at": 0},
    ),
    (
        # Realistic data. Look like a created object
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "created_at": 1581002681,
            "updated_at": 1581002681,
        },
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "created_at": 1581002681,
            "updated_at": 1581002681,
        },
    ),
    (
        # Here is a modified object
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "created_at": 1581002681,
            "updated_at": 2600000000,
        },
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "created_at": 1581002681,
            "updated_at": 2600000000,
        },
    ),
]

data_error_args = [
    (
        # updated_at cannot be explicitly before created_at
        {"_id": None, "created_at": 10, "updated_at": 5}
    ),
    (
        # Nor implicitly
        {"_id": None, "created_at": None, "updated_at": 5}
    ),
]
