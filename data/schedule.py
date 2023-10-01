from datetime import datetime

from data.schema import Data, Team, User, Duty
from src.api.enums import Role

data = Data(
    teams=[
        Team(
            name='k8s_SRE',
            scheduling_timezone='Europe/Moscow',
            email='k8s@sre-course.ru',
            slack_channel='#k8s-team',
            roster='k8s',
            users=[
                User(
                    name='o.ivanov',
                    full_name='Oleg Ivanov',
                    phone_number='+1 111-111-1111',
                    email='o.ivanov@sre-course.ru',
                    duties=[
                        Duty(
                            date=datetime(2023, 10, 2),
                            role=Role.PRIMARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 3),
                            role=Role.SECONDARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 4),
                            role=Role.PRIMARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 5),
                            role=Role.SECONDARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 6),
                            role=Role.PRIMARY,
                        ),
                    ]
                ),
                User(
                    name='d.petrov',
                    full_name='Dmitriy Petrov',
                    phone_number='+1 211-111-1111',
                    email='d.petrov@sre-course.ru',
                    duties=[
                        Duty(
                            date=datetime(2023, 10, 2),
                            role=Role.SECONDARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 3),
                            role=Role.PRIMARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 4),
                            role=Role.SECONDARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 5),
                            role=Role.PRIMARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 6),
                            role=Role.SECONDARY,
                        ),
                    ]
                ),
            ]
        ),
        Team(
            name='DBA_SRE',
            scheduling_timezone='Asia/Novosibirsk',
            email='dba@sre-course.ru',
            slack_channel='#dba-team',
            roster='DBA',
            users=[
                User(
                    name='a.seledkov',
                    full_name='Alexander Seledkov',
                    phone_number='+1 311-111-1111',
                    email='a.seledkov@sre-course.ru',
                    duties=[
                        Duty(
                            date=datetime(2023, 10, 2),
                            role=Role.PRIMARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 3),
                            role=Role.PRIMARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 4),
                            role=Role.PRIMARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 5),
                            role=Role.SECONDARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 6),
                            role=Role.PRIMARY,
                        ),
                    ]
                ),
                User(
                    name='d.hludeev',
                    full_name='Dmitriy Hludeev',
                    phone_number='+1 411-111-1111',
                    email='user-4@sre-course.ru',
                    duties=[
                        Duty(
                            date=datetime(2023, 10, 2),
                            role=Role.SECONDARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 3),
                            role=Role.SECONDARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 4),
                            role=Role.VACATION,
                        ),
                        Duty(
                            date=datetime(2023, 10, 5),
                            role=Role.PRIMARY,
                        ),
                        Duty(
                            date=datetime(2023, 10, 6),
                            role=Role.SECONDARY,
                        ),
                    ]
                ),
            ]
        )
    ]
)
