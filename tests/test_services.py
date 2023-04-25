from src.userservice.adapters.services.users import UsersService


def test_user_is_saved():
    users = UsersService()
    user_id = users.register_user("Shako Rzayev", "rzayev.sehriyar@gmail.com", password="12345")
    assert user_id


def test_get_user():
    users = UsersService()
    user_id = users.register_user("Shako Rzayev", "rzayev.sehriyar@gmail.com", password="12345")
    user_ = users.get_user(user_id)
    assert user_.is_active
    assert user_.email == "rzayev.sehriyar@gmail.com"


def test_update_user():
    users = UsersService()
    user_id = users.register_user("Shako Rzayev", "rzayev.sehriyar@gmail.com", password="12345")
    user_ = users.get_user(user_id)
    assert user_.is_active
    assert user_.full_name == "Shako Rzayev"
    users.update_user(user_id, "Shahriyar Rzayev")
    user_ = users.get_user(user_id)
    assert user_.is_active
    assert user_.full_name == "Shahriyar Rzayev"


def test_deactivate_user():
    users = UsersService()
    user_id = users.register_user("Shako Rzayev", "rzayev.sehriyar@gmail.com", password="12345")
    user_ = users.get_user(user_id)
    assert user_.is_active
    assert user_.full_name == "Shako Rzayev"
    users.deactivate_user(user_id)
    user_ = users.get_user(user_id)
    assert not user_.is_active
