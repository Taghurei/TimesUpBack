from core.exceptions import TimesUpException


class IncorrectCredentialsException(TimesUpException):
    def __init__(self, error_code: int):
        self.error_code = error_code
        self.external_message = "Incorrect credentials"
        self.internal_message = "Given credentials do not match"
        status_code = 500

    def __str__(self):
        return self.internal_message


class BadPermissionException(TimesUpException):
    def __init__(self, error_code: int):
        self.error_code = error_code
        self.external_message = "You cannot do this"
        self.internal_message = "Someone tried to access a resource he has no right on"

        # Maybe authentified but has not the right permissions
        status_code = 403

    def __str__(self):
        return self.internal_message