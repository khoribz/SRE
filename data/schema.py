from datetime import datetime

from pydantic import BaseModel

from src.api.enums import Role


class Duty(BaseModel):
    date: datetime
    role: Role


class User(BaseModel):
    name: str
    full_name: str
    phone_number: str
    email: str
    duties: list[Duty]


class Team(BaseModel):
    name: str
    scheduling_timezone: str
    email: str
    slack_channel: str
    roster: str
    users: list[User]


class Data(BaseModel):
    teams: list[Team]
