from core.exceptions import TimesUpException


class TimesUpTeamsException(TimesUpException):
    def __init__(self, error_code: int = 1):
        self.error_code = error_code
        self.internal_message = (
            "Teams Exception: There should only be 2 teams with at least 1 player"
        )
        self.external_message = (
            "There should only be 2 teams, with at least 1 player in each"
        )
        self.status_code = 400

    def __str__(self):
        return self.internal_message


class TimesUpGameNotFoundException(TimesUpException):
    def __init__(self, error_code: int = 30):
        self.error_code = error_code
        self.internal_message = "TimesUpGameNotFoundException: no game matches"
        self.external_message = "No open game found"
        self.status_code = 404

    def __str__(self):
        return self.internal_message


class TimesUpNotGameOwnerException(TimesUpException):
    def __init__(self, error_code: int = 31):
        self.error_code = error_code
        self.internal_message = (
            "TimesUpNotGameOwnerException: only the host can do that on this game"
        )
        self.external_message = "Only the host can start this game"
        self.status_code = 403

    def __str__(self):
        return self.internal_message


class TimesUpGameAlreadyStartedException(TimesUpException):
    def __init__(self, error_code: int = 32):
        self.error_code = error_code
        self.internal_message = (
            "TimesUpGameAlreadyStartedException: the game is no longer a lobby"
        )
        self.external_message = "This game has already started"
        self.status_code = 409

    def __str__(self):
        return self.internal_message


class TimesUpEmptyLobbyException(TimesUpException):
    def __init__(self, error_code: int = 37):
        self.error_code = error_code
        self.internal_message = (
            "TimesUpEmptyLobbyException: the lobby has no word to play with"
        )
        self.external_message = "Add at least one word before starting the game"
        self.status_code = 400

    def __str__(self):
        return self.internal_message


class TimesUpMissingPlayerNameException(TimesUpException):
    def __init__(self, error_code: int = 36):
        self.error_code = error_code
        self.internal_message = (
            "TimesUpMissingPlayerNameException: a player joined without a name"
        )
        self.external_message = "Tell us your name to join the game"
        self.status_code = 400

    def __str__(self):
        return self.internal_message


class TimesUpUnknownTeamException(TimesUpException):
    def __init__(self, error_code: int = 33, team: str = ""):
        self.error_code = error_code
        self.internal_message = (
            "TimesUpUnknownTeamException: unknown team " + str(team)
        )
        self.external_message = "Pick either team1 or team2"
        self.status_code = 400

    def __str__(self):
        return self.internal_message
