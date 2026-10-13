from main import login, register, main, handle_choice, show_menu
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

def test_main_exit(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "0")

    main()

    captured = capsys.readouterr()

    assert "Goodbye!" in captured.out

def test_handle_choice_total_value(capsys):
    products = [
        {"name": "Keyboard", "quantity": 2, "price": 100}
    ]

    handle_choice("2", products)

    captured = capsys.readouterr()
    assert "Total warehouse value: 200 zł" in captured.out

def test_handle_choice_invalid_option(capsys):
    products = []

    handle_choice("x", products)

    captured = capsys.readouterr()
    assert "Invalid option." in captured.out

def test_handle_choice_search_product(monkeypatch, capsys):
    products = [
        {"name": "Keyboard", "quantity": 2, "price": 100}
    ]

    monkeypatch.setattr("builtins.input", lambda _: "Keyboard")

    handle_choice("5", products)

    captured = capsys.readouterr()
    assert "Product found: Keyboard - 100 zł" in captured.out

def test_handle_choice_search_product_not_found(monkeypatch, capsys):
    products = [
        {"name": "Keyboard", "quantity": 2, "price": 100}
    ]

    monkeypatch.setattr("builtins.input", lambda _: "Tablet")

    handle_choice("5", products)

    captured = capsys.readouterr()
    assert "Product not found." in captured.out

def test_handle_choice_show_products(capsys):
    products = [
        {"name": "Keyboard", "quantity": 2, "price": 100}
    ]

    handle_choice("1", products)

    captured = capsys.readouterr()
    assert "Keyboard" in captured.out

def test_handle_choice_most_expensive(capsys):
    products = [
        {"name": "Keyboard", "quantity": 2, "price": 100},
        {"name": "Monitor", "quantity": 1, "price": 1200}
    ]

    handle_choice("4", products)

    captured = capsys.readouterr()
    assert "Most expensive: Monitor - 1200 zł" in captured.out

def test_handle_choice_low_stock(capsys):
    products = [
        {"name": "Keyboard", "quantity": 2, "price": 100},
        {"name": "Monitor", "quantity": 10, "price": 1200}
    ]

    handle_choice("3", products)

    captured = capsys.readouterr()
    assert "Keyboard" in captured.out
    assert "Monitor" not in captured.out

def test_handle_choice_add_product(monkeypatch, capsys):
    products = []

    inputs = iter(["Keyboard", "3", "100"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    handle_choice("6", products)

    captured = capsys.readouterr()

    assert "Product added successfully." in captured.out
    assert products[0]["name"] == "Keyboard"
    assert products[0]["quantity"] == 3
    assert products[0]["price"] == 100

def test_handle_choice_add_existing_product(monkeypatch, capsys):
    products = [
        {"name": "Keyboard", "quantity": 2, "price": 100}
    ]

    inputs = iter(["Keyboard", "3", "100"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    handle_choice("6", products)

    captured = capsys.readouterr()

    assert "Product already exists." in captured.out
    assert len(products) == 1

def test_handle_choice_update_quantity(monkeypatch, capsys):
    products = [
        {"name": "Keyboard", "quantity": 2, "price": 100}
    ]

    inputs = iter(["Keyboard", "10"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    handle_choice("7", products)

    captured = capsys.readouterr()

    assert "Quantity updated successfully." in captured.out
    assert products[0]["quantity"] == 12

def test_handle_choice_update_quantity_not_found(monkeypatch, capsys):
    products = [
        {"name": "Keyboard", "quantity": 2, "price": 100}
    ]

    inputs = iter(["Tablet", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    handle_choice("7", products)

    captured = capsys.readouterr()

    assert "Product not found." in captured.out
    assert len(products) == 1
    assert products[0]["quantity"] == 2

def test_handle_choice_sell_product(monkeypatch, capsys):
    products = [
        {"name": "Keyboard", "quantity": 10, "price": 100}
    ]

    inputs = iter(["Keyboard", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    handle_choice("8", products)

    captured = capsys.readouterr()

    assert "Product sold successfully." in captured.out
    assert products[0]["quantity"] == 7

def test_handle_choice_sell_product_not_enough_stock(monkeypatch, capsys):
    products = [
        {"name": "Keyboard", "quantity": 2, "price": 100}
    ]

    inputs = iter(["Keyboard", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    handle_choice("8", products)

    captured = capsys.readouterr()

    assert "Not enough stock." in captured.out
    assert products[0]["quantity"] == 2

def test_handle_choice_delete_product(monkeypatch, capsys):
    products = [
        {"name": "Keyboard", "quantity": 2, "price": 100}
    ]

    monkeypatch.setattr("builtins.input", lambda _: "Keyboard")

    handle_choice("9", products)

    captured = capsys.readouterr()

    assert "Product deleted successfully." in captured.out
    assert len(products) == 0


def test_handle_choice_delete_product_not_found(monkeypatch, capsys):
    products = [
        {"name": "Keyboard", "quantity": 2, "price": 100}
    ]

    monkeypatch.setattr("builtins.input", lambda _: "Tablet")

    handle_choice("9", products)

    captured = capsys.readouterr()

    assert "Product not found." in captured.out
    assert len(products) == 1


def test_show_menu(capsys):
    show_menu("TEST WAREHOUSE")

    captured = capsys.readouterr()

    assert "TEST WAREHOUSE" in captured.out
    assert "1. Show products" in captured.out
    assert "5. Search product" in captured.out
    assert "9. Delete product" in captured.out
    assert "0. Exit" in captured.out


def test_handle_choice_sell_product_not_found(monkeypatch, capsys):
    products = [
        {"name": "Keyboard", "quantity": 10, "price": 100}
    ]

    inputs = iter(["Tablet", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    handle_choice("8", products)

    captured = capsys.readouterr()

    assert "Product not found." in captured.out
    assert products[0]["quantity"] == 10


def test_main_invalid_option(monkeypatch, capsys):
    inputs = iter(["x", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    captured = capsys.readouterr()

    assert "Invalid option." in captured.out
    assert "Goodbye!" in captured.out


def test_main_login_failed(monkeypatch, capsys):
    monkeypatch.setattr("main.login", lambda users: None)

    inputs = iter(["1", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    captured = capsys.readouterr()

    assert "Login failed. Try again." in captured.out
    assert "Goodbye!" in captured.out


def test_main_register_option(monkeypatch, capsys):
    register_calls = []

    monkeypatch.setattr(
        "main.register",
        lambda users: register_calls.append(users)
    )

    inputs = iter(["2", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    captured = capsys.readouterr()

    assert len(register_calls) == 1
    assert "Goodbye!" in captured.out


def test_main_login_success(monkeypatch, capsys):
    monkeypatch.setattr("main.login", lambda users: "marcin@example.com")

    inputs = iter(["1", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    captured = capsys.readouterr()

    assert "MY WAREHOUSE" in captured.out
    assert "Goodbye!" in captured.out

