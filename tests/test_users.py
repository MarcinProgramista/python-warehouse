from users import (
    register_user,
    login_user,
    normalize_email,
    is_valid_email,
    is_valid_password,
    hash_password,
    verify_password,
    SUCCESS,
    INVALID_EMAIL,
    INVALID_PASSWORD,
    EMAIL_ALREADY_EXISTS,
    INVALID_CREDENTIALS
)

def test_login_user_success():
    users = {}

    register_user(
        users,
        "marcin@example.com",
        "password1234"
    )

    result = login_user(
        users,
        "marcin@example.com",
        "password1234"
    )

    assert result == SUCCESS


def test_register_user_duplicate_email():
    users = {}

    first_result = register_user(
        users,
        "marcin@example.com",
        "password1234"
    )

    second_result = register_user(
        users,
        " MARCIN@EXAMPLE.COM",
        "anotherpassword"
    )

    assert first_result == SUCCESS
    assert second_result == EMAIL_ALREADY_EXISTS
    assert len(users) == 1


def test_register_user_invalid_password():
    users = {}

    result = register_user(
        users,
        "marcin@example.com",
        "123"
    )

    assert result == INVALID_PASSWORD
    assert users == {}


def test_register_user_invalid_email():
    users = {}

    result = register_user(
        users,
        "marcin",
        "password1234"
    )

    assert result == INVALID_EMAIL
    assert users == {}


def test_register_user_normalizes_email():
    users = {}

    result = register_user(
        users,
        "  MARCIN@EXAMPLE.COM",
        "password1234"
    )

    assert result == SUCCESS
    assert "marcin@example.com" in users


def test_verify_password():
    password = "password1234"
    hashed_password = hash_password(password)

    assert verify_password(password, hashed_password) is True


def test_verify_wrong_password():
    password = "password1234"
    hashed_password = hash_password(password)

    assert verify_password("wrongpassword", hashed_password) is False


def test_hash_password():
    password = "password1234"

    hashed_password = hash_password(password)

    assert hashed_password != password


def test_register_user():
    users = {}

    result = register_user(
        users,
        "marcin@example.com",
        "password1234"
    )

    assert result == SUCCESS
    assert users["marcin@example.com"] != "password1234"
    assert verify_password(
        "password1234",
        users["marcin@example.com"]
    ) is True


def test_normalize_email():
    result = normalize_email(" MARCIN@EXAMPLE.COM")

    assert result == "marcin@example.com"


def test_is_valid_email():
    assert is_valid_email("marcin@example.com") is True


def test_is_invalid_email():
    assert is_valid_email("marcin") is False
    assert is_valid_email("marcin@") is False
    assert is_valid_email("@example.com") is False
    assert is_valid_email("marcin@example") is False
    assert is_valid_email("marcin@@example.com") is False


def test_is_valid_password():
    assert is_valid_password("password1234") is True


def test_is_invalid_password():
    assert is_valid_password("1234567") is False
    assert is_valid_password("        ") is False


def test_hash_password_is_different_each_time():
    password = "password1234"

    hash_1 = hash_password(password)
    hash_2 = hash_password(password)

    assert hash_1 != hash_2

def test_login_user_wrong_password():
    users = {}
    register_user(users, "marcin@example.com", "password1234")

    result = login_user(
        users,
        "marcin@example.com",
        "wrongpassword123"
    )

    assert result == INVALID_CREDENTIALS

def test_login_user_not_found():
    users = {}

    result = login_user(
        users,
        "unknown@example.com",
        "password1234"
    )

    assert result == INVALID_CREDENTIALS

def test_login_user_normalizes_email():
    users = {}

    register_user(
        users,
        "marcin@example.com",
        "password1234"
    )

    result = login_user(
        users,
        "MARCIN@EXAMPLE.COM",
        "password1234"
    )

    assert result == SUCCESS

def test_login_user_wrong_password_does_not_change_users():
    users = {}
    register_user(
        users,
        "marcin@example.com",
        "password1234"
    )

    users_before = users.copy()

    login_user(
        users,
        "marcin@example.com",
        "wrongpassword123"
    )

    assert users == users_before
