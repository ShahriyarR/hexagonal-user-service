from uuid import uuid4

from eventsourcing.domain import Aggregate

from userservice.domain.model.events import (Registered, UserDeactivated,
                                             UserUpdated)

from userservice.domain.model.domain import Password


class User(Aggregate):
    def __init__(self, full_name: str, email: str, password: str):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.is_active = True

    @classmethod
    def register(cls, full_name: str, email: str, password: Password) -> "User":
        return cls._create(
            Registered,
            id=uuid4(),
            full_name=full_name,
            email=email,
            password=password.get_secret(),
        )

    def update(self, full_name: str) -> None:
        self.trigger_event(UserUpdated, full_name=full_name)

    def deactivate(self, is_active: bool = False):
        self.trigger_event(UserDeactivated, is_active=is_active)
