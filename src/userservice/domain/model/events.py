from eventsourcing.domain import AggregateCreated, AggregateEvent


class Registered(AggregateCreated):
    full_name: str
    email: str


class UserUpdated(AggregateEvent):
    full_name: str

    def apply(self, aggregate: "User") -> None:
        aggregate.full_name = self.full_name


class UserDeactivated(AggregateEvent):
    is_active: bool

    def apply(self, aggregate: "User") -> None:
        aggregate.is_active = self.is_active
