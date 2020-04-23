from core.exceptions import TimesUpException


class TimesUpTeamsException(TimesUpException):
    def __init__(self, error_code: int = 1):
        error_code = 1
        external_message = "Unknown Error"
        internal_message = (
            "Teams Exception: There should only be 2 teams with at least 1 player"
        )
        status_code = 500

    def __str__(self):
        return self.internal_message
