from users import register_user

def test_register_user():
    users = {}

    result = register_user(users, "marcin", "1234")

    assert result is True
    assert users["marcin"] == "1234"