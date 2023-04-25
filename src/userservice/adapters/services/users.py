from uuid import UUID

from eventsourcing.application import AggregateNotFound, Application

from userservice.domain.model.aggregate import User
from userservice.domain.model.exceptions import UserAccountNotFoundError
from userservice.domain.ports.services.users import UsersServiceInterface


class UsersService(Application, UsersServiceInterface):
    def _register_user(self, full_name: str, email: str) -> UUID:
        user = User.register(
            full_name=full_name,
            email=email,
        )
        self.save(user)
        return user.id

    def _get_user(self, user_id: UUID) -> User:
        try:
            aggregate = self.repository.get(user_id)
        except AggregateNotFound as err:
            raise UserAccountNotFoundError(user_id) from err
        else:
            assert isinstance(aggregate, User)
            return aggregate

    def _update_user(self, user_id: UUID, full_name: str) -> User:
        aggregate = self.get_user(user_id)
        aggregate.update(full_name)
        self.save(aggregate)
        return aggregate

    def _deactivate_user(self, user_id: UUID) -> User:
        aggregate = self.get_user(user_id)
        aggregate.deactivate()
        self.save(aggregate)
        return aggregate
