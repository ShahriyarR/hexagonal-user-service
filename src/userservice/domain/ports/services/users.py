from abc import ABC, abstractmethod
from uuid import UUID

from userservice.domain.model.aggregate import User


class UsersServiceInterface(ABC):
    def register_user(self, full_name: str, email: str, password: str) -> UUID:
        return self._register_user(full_name, email, password)

    def get_user(self, user_id: UUID) -> User:
        return self._get_user(user_id)

    def update_user(self, user_id: UUID, full_name: str) -> User:
        return self._update_user(user_id, full_name)

    def deactivate_user(self, user_id: UUID) -> User:
        return self._deactivate_user(user_id)

    @abstractmethod
    def _register_user(self, full_name: str, email: str, password: str) -> UUID:
        raise NotImplementedError

    @abstractmethod
    def _get_user(self, user_id: UUID) -> User:
        raise NotImplementedError

    @abstractmethod
    def _update_user(self, user_id: UUID, full_name: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def _deactivate_user(self, user_id: UUID) -> User:
        raise NotImplementedError
