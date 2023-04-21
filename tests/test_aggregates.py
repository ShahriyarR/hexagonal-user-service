from userservice.domain.model.aggregate import User


def test_if_aggregate_created():
    user = User(full_name="Shako Rzayev", email="rzayev.sehriyar@gmail.com")
    user_ = User(full_name="Ildirim Rzayev", email="no_email@example.com")
    assert user.is_active
    assert user_.is_active
    assert user is not user_


def test_if_aggregate_registered():
    user_registered = User.register(
        full_name="Shako Rzayev", email="rzayev.sehriyar@gmail.com"
    )
    assert user_registered.is_active


def test_if_aggregate_updated():
    user_registered = User.register(
        full_name="Shako Rzayev", email="rzayev.sehriyar@gmail.com"
    )
    assert user_registered.version == 1
    user_registered.update("New Name")
    assert user_registered.version == 2
    assert user_registered.full_name == "New Name"


def test_if_aggregate_deactivated():
    user_registered = User.register(
        full_name="Shako Rzayev", email="rzayev.sehriyar@gmail.com"
    )
    assert user_registered.version == 1
    user_registered.deactivate()
    assert user_registered.version == 2
    assert not user_registered.is_active
