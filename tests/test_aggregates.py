import pytest
from readonce import UnsupportedOperationException

from userservice.domain.model.aggregate import User
from userservice.domain.model.domain import Password


def test_if_aggregate_created():
    user = User(
        full_name="Shako Rzayev",
        email="rzayev.sehriyar@gmail.com",
        password="12345",
    )
    user_ = User(
        full_name="Ildirim Rzayev",
        email="no_email@example.com",
        password="12345",
    )
    assert user.is_active
    assert user_.is_active
    assert user is not user_
    assert user.version == 1
    assert user_.version == 1


def test_if_aggregate_password_has_proper_type():
    user = User(
        full_name="Shako Rzayev",
        email="rzayev.sehriyar@gmail.com",
        password="12345",
    )
    assert isinstance(user.password, Password)
    assert user.password.get_secret() == "12345"
    with pytest.raises(UnsupportedOperationException):
        assert user.password.get_secret() == "12345"


def test_if_aggregate_registered():
    user_registered = User.register(
        full_name="Shako Rzayev",
        email="rzayev.sehriyar@gmail.com",
        password="12345",
    )
    assert user_registered.is_active
    assert user_registered.version == 1


def test_if_aggregate_updated():
    user_registered = User.register(
        full_name="Shako Rzayev",
        email="rzayev.sehriyar@gmail.com",
        password="12345",
    )
    assert user_registered.version == 1
    user_registered.update("New Name")
    assert user_registered.version == 2
    assert user_registered.full_name == "New Name"


def test_if_aggregate_deactivated():
    user_registered = User.register(
        full_name="Shako Rzayev",
        email="rzayev.sehriyar@gmail.com",
        password="12345",
    )
    assert user_registered.version == 1
    user_registered.deactivate()
    assert user_registered.version == 2
    assert not user_registered.is_active


def test_reconstruct_aggregate_from_events():
    user_registered = User.register(
        full_name="Shako Rzayev",
        email="rzayev.sehriyar@gmail.com",
        password="12345",
    )
    assert user_registered.version == 1
    user_registered.update("New Name")
    assert user_registered.version == 2
    user_registered.deactivate()
    assert user_registered.version == 3
    events = user_registered.collect_events()
    copy = None
    for event in events:
        copy = event.mutate(copy)
    # even you get the same user they are not the same objects
    assert copy is not user_registered
    assert copy.full_name == "New Name"
    assert not copy.is_active


def test_reconstruct_aggregate_from_events_password_operations():
    user_registered = User.register(
        full_name="Shako Rzayev",
        email="rzayev.sehriyar@gmail.com",
        password="12345",
    )
    assert user_registered.version == 1
    user_registered.update("New Name")
    assert user_registered.version == 2
    user_registered.deactivate()
    assert user_registered.version == 3
    assert user_registered.password.get_secret() == "12345"
    with pytest.raises(UnsupportedOperationException):
        assert user_registered.password.get_secret() == "12345"
    user_registered.update("PyBerlin")

    events = user_registered.collect_events()
    copy = None
    for event in events:
        copy = event.mutate(copy)
    # even you get the same user they are not the same objects
    assert copy is not user_registered
    assert copy.full_name == "PyBerlin"
    assert not copy.is_active
    assert isinstance(copy.password, Password)
    assert copy.password.get_secret() == "12345"
    with pytest.raises(UnsupportedOperationException):
        assert copy.password.get_secret() == "12345"
