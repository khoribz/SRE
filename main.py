import time
from datetime import timedelta

from data.schedule import data
from src.api.schema import (
    CreateTeamRequest, CreateUserRequest, CreateRosterRequest, BindUserRequest,
    Contacts, UpdateUserRequest, CreateEventRequest,
)
from src.clients.base_client import BaseClient


def create_oncall_schedule() -> None:
    client = BaseClient()

    for team in data.teams:
        client.create_team(
            CreateTeamRequest(
                name=team.name,
                scheduling_timezone=team.scheduling_timezone,
                email=team.email,
                slack_channel=team.slack_channel,
            )
        )
        client.create_roster(
            request=CreateRosterRequest(name=team.roster),
            team=team.name
        )
        for user in team.users:
            client.create_user(
                request=CreateUserRequest(name=user.name),
            )
            client.bind_user(
                request=BindUserRequest(user_name=user.name),
                team=team.name,
                roster=team.roster,
            )
            client.update_user(
                request=UpdateUserRequest(
                    name=user.name,
                    full_name=user.full_name,
                    contacts=Contacts(
                        call=user.phone_number,
                        email=user.email,
                    ),
                    active=1,
                ),
                name=user.name
            )
            for duty in user.duties:
                client.create_event(
                    request=CreateEventRequest(
                        start=time.mktime(duty.date.timetuple()),
                        end=time.mktime((duty.date + timedelta(days=1)).timetuple()),
                        user=user.name,
                        team=team.name,
                        role=duty.role,
                    )
                )


if __name__ == '__main__':
    create_oncall_schedule()
