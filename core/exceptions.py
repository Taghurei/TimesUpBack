class TimesUpException(Exception):
    error_code = 0
    external_message = "Unknown Error"
    internal_message = "Something went wrong here"
    status_code = 500


class TimesUpDateException(TimesUpException):
    def __init__(self, error_code: int = 1):
        error_code = 1
        external_message = "Unknown Error"
        internal_message = "Dates Exception: Creation date is after update date"
        status_code = 500

    def __str__(self):
        return self.internal_message


class TimesUpEmptyFieldException(TimesUpException):
    def __init__(self, error_code: int, blank_field: str):
        self.external_message = "Unknown Error"
        self.internal_message = (
            "TimesUpEmptyFieldException: The following field was blank : " + blank_field
        )
        self.status_code = 500
        self.error_code = error_code

    def __str__(self):
        return self.internal_message


class TimesUpTypeException(TimesUpException):
    def __init__(self, error_code: int, incorrect_input: str):
        self.error_code = error_code
        self.internal_message = (
            "TimesUpTypeException: the following input did not respect the right type : "
            + incorrect_input
        )
        self.external_message = "Unknown Error"
        self.status_code = 500

    def __str__(self):
        return self.internal_message

class TimesUpUnexpectedNegativeValue(TimesUpException):
    def __init__(self, error_code: int, incorrect_input: str):
        self.error_code = error_code
        self.internal_message = (
            "TimesUpUnexpectedNegativeValue: the following input has a negative value : "
            + incorrect_input
        )
        self.external_message = "Unknown Error"
        self.status_code = 500

    def __str__(self):
        return self.internal_message

class TimesUpNotUniqueException(TimesUpException):
    def __init__(self, error_code: int):
        self.error_code = error_code
        self.internal_message = "The object has not been created / updated in db because another object exists with the same set of unique fields"
        self.external_message = "Object not created / updated"
        self.status_code = 500

    def __str__(self):
        return self.internal_message
