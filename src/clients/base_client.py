import json

from requests import Session

import settings

from src.api.enums import OncallRoutes
from src.api.schema import (
    CreateTeamRequest, LoginRequest, CreateUserRequest, CreateRosterRequest, BindUserRequest, UpdateUserRequest,
    CreateEventRequest,
)
from src.api.wrappers import api_wrapper


class BaseClient:
    def __init__(self):
        self.base_url = settings.ONCALL_BASE_URL
        self.api_url = f'api/{settings.ONCALL_API_VERSION}/'
        self.session = Session()
        self.headers = {
            'Content-Type': 'application/json',
            'x-csrf-token': self._get_csrf_token(
                LoginRequest(username=settings.ONCALL_USERNAME, password=settings.ONCALL_PASSWORD)
            )
        }

    @api_wrapper(LoginRequest)
    def _get_csrf_token(self, request: LoginRequest) -> str:
        response = self.session.post(
            url=f'{self.base_url}/{OncallRoutes.LOGIN}',
            data=request.model_dump()
        )
        return response.json().get('csrf_token')

    @api_wrapper(CreateTeamRequest)
    def create_team(self, request: CreateTeamRequest) -> None:
        self.session.post(
            url=f'{self.base_url}{self.api_url}{OncallRoutes.TEAMS}',
            headers=self.headers,
            data=request.model_dump_json()
        )

    @api_wrapper(CreateRosterRequest)
    def create_roster(self, request: CreateRosterRequest, team: str) -> None:
        self.session.post(
            url=f'{self.base_url}{self.api_url}{OncallRoutes.TEAMS}/{team}/{OncallRoutes.ROSTERS}',
            headers=self.headers,
            data=json.dumps({'name': request.name})
        )

    @api_wrapper(CreateUserRequest)
    def create_user(self, request: CreateUserRequest) -> None:
        self.session.post(
            url=f'{self.base_url}{self.api_url}{OncallRoutes.USERS}',
            headers=self.headers,
            data=request.model_dump_json()
        )

    @api_wrapper(UpdateUserRequest)
    def update_user(self, request: UpdateUserRequest, name: str) -> None:
        self.session.put(
            url=f'{self.base_url}{self.api_url}{OncallRoutes.USERS}/{name}',
            headers=self.headers,
            data=request.model_dump_json()
        )

    @api_wrapper(BindUserRequest)
    def bind_user(self, request: BindUserRequest, team: str, roster: str) -> None:
        self.session.post(
            url=(
                f'{self.base_url}{self.api_url}{OncallRoutes.TEAMS}/{team}/{OncallRoutes.ROSTERS}/'
                f'{roster}/{OncallRoutes.USERS}'
            ),
            headers=self.headers,
            data=json.dumps({'name': request.user_name})
        )

    @api_wrapper(CreateEventRequest)
    def create_event(self, request: CreateEventRequest) -> None:
        self.session.post(
            url=f'{self.base_url}{self.api_url}{OncallRoutes.EVENTS}',
            headers=self.headers,
            data=request.model_dump_json()
        )
