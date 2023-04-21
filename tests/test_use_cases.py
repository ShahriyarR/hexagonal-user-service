from src.userservice.adapters.services.users import UsersService


def test_user_is_saved():
    users = UsersService()
    user_id = users.register_user("Shako Rzayev", "rzayev.sehriyar@gmail.com")
    assert user_id


def test_get_user():
    users = UsersService()
    user_id = users.register_user("Shako Rzayev", "rzayev.sehriyar@gmail.com")
    user_ = users.get_user(user_id)
    assert user_.is_active
    assert user_.email == "rzayev.sehriyar@gmail.com"
