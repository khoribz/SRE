from enum import Enum


class OncallRoutes(str, Enum):
    LOGIN = 'login'
    ROSTERS = 'rosters'
    TEAMS = 'teams'
    USERS = 'users'
    EVENTS = 'events'

    def __str__(self) -> str:
        return str.__str__(self)


class Role(str, Enum):
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    VACATION = 'vacation'
