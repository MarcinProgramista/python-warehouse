from main import login
from users import register_user, SUCCESS

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
