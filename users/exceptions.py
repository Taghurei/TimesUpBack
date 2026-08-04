from core.exceptions import TimesUpException


class TimesUpNicknameTakenException(TimesUpException):
    def __init__(self, error_code: int = 22):
        self.error_code = error_code
        self.internal_message = (
            "TimesUpNicknameTakenException: a user already exists with this nickname"
        )
        self.external_message = "This nickname is already taken"
        self.status_code = 409

    def __str__(self):
        return self.internal_message


class TimesUpWrongCredentialsException(TimesUpException):
    def __init__(self, error_code: int = 23):
        self.error_code = error_code
        self.internal_message = (
            "TimesUpWrongCredentialsException: unknown nickname or wrong password"
        )
        self.external_message = "Wrong nickname or password"
        self.status_code = 401

    def __str__(self):
        return self.internal_message


class TimesUpNotLoggedInException(TimesUpException):
    def __init__(self, error_code: int = 24):
        self.error_code = error_code
        self.internal_message = (
            "TimesUpNotLoggedInException: this route needs a valid Authorization token"
        )
        self.external_message = "You need to be logged in to do that"
        self.status_code = 401

    def __str__(self):
        return self.internal_message


class TimesUpWeakPasswordException(TimesUpException):
    def __init__(self, error_code: int = 25, minimum_length: int = 4):
        self.error_code = error_code
        self.internal_message = (
            "TimesUpWeakPasswordException: the password is shorter than "
            + str(minimum_length)
            + " characters"
        )
        self.external_message = (
            "Your password needs at least " + str(minimum_length) + " characters"
        )
        self.status_code = 400

    def __str__(self):
        return self.internal_message
