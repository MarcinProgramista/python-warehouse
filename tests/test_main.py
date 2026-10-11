from main import login, register
from users import register_user


def test_login_success(monkeypatch):
    users = {}
    register_user(users, "test@example.com", "StrongPassword123!")

    inputs = iter(["test@example.com", "StrongPassword123!"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = login(users)

    assert result == "test@example.com"

def test_login_wrong_password(monkeypatch):
    users = {}
    register_user(users, "test@example.con", "StrongPassword123!")

    inputs = iter(["test@exampl.com", "WrongPassword123!"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = login(users)

    assert result is None

def test_login_unknown_user(monkeypatch):
    users = {}

    inputs = iter(["unknown@example.com", "StrongPassword123!"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = login(users)

    assert result is None

def test_register_success(monkeypatch):
    users = {}
    inputs = iter(["new@example.com", "StrongPassword123!"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = register(users)

    assert result is True
    assert "new@example.com" in users


def test_register_existing_email(monkeypatch):
    users = {}
    register_user(users, "test@example.com", "StrongPassword123!")

    inputs = iter(["test@example.com", "AnotherPassword123!"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = register(users)

    assert result is False
