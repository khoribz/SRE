from pydantic import BaseModel, field_validator

from src.api.enums import Role


class LoginRequest(BaseModel):
    username: str
    password: str


class CreateTeamRequest(BaseModel):
    name: str
    scheduling_timezone: str
    email: str
    slack_channel: str


class CreateRosterRequest(BaseModel):
    name: str


class BindUserRequest(BaseModel):
    user_name: str


class Contacts(BaseModel):
    call: str
    email: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, value: str) -> str:
        if '@' not in value:
            raise ValueError('email validation error')
        return value


class UpdateUserRequest(BaseModel):
    name: str
    full_name: str
    contacts: Contacts | None
    active: int


class CreateUserRequest(BaseModel):
    name: str


class CreateEventRequest(BaseModel):
    start: int
    end: int
    user: str
    team: str
    role: Role
