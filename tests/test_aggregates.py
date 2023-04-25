from userservice.domain.model.aggregate import User

from userservice.domain.model.domain import Password


def test_if_aggregate_created():
    user = User(
        full_name="Shako Rzayev", email="rzayev.sehriyar@gmail.com", password=Password("12345")
    )
    user_ = User(
        full_name="Ildirim Rzayev", email="no_email@example.com", password=Password("12345")
    )
    assert user.is_active
    assert user_.is_active
    assert user is not user_
    assert user.version == 1
    assert user_.version == 1


def test_if_aggregate_registered():
    user_registered = User.register(
        full_name="Shako Rzayev", email="rzayev.sehriyar@gmail.com", password=Password("12345")
    )
    assert user_registered.is_active
    assert user_registered.version == 1


def test_if_aggregate_updated():
    user_registered = User.register(
        full_name="Shako Rzayev", email="rzayev.sehriyar@gmail.com", password=Password("12345")
    )
    assert user_registered.version == 1
    user_registered.update("New Name")
    assert user_registered.version == 2
    assert user_registered.full_name == "New Name"


def test_if_aggregate_deactivated():
    user_registered = User.register(
        full_name="Shako Rzayev", email="rzayev.sehriyar@gmail.com", password=Password("12345")
    )
    assert user_registered.version == 1
    user_registered.deactivate()
    assert user_registered.version == 2
    assert not user_registered.is_active


def test_reconstruct_aggregate_from_events():
    user_registered = User.register(
        full_name="Shako Rzayev", email="rzayev.sehriyar@gmail.com", password=Password("12345")
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
