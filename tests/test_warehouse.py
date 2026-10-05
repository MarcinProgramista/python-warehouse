from warehouse import search_product, add_product, update_quantity, sell_product, delete_product
from utils import get_positive_int

def test_search_product_found():
    products = [
        {"name": "Laptop", "quantity": 10, "price": 1500},
        {"name": "Monitor", "quantity": 2, "price": 1200},
    ]

    result = search_product(products, "Laptop")
    assert result["name"] == "Laptop"

def test_search_product_not_found():
    products = [
        {"name": "Laptop", "quantity": 10, "price": 1500},
        {"name": "Monitor", "quantity": 2, "price": 1200},
    ]

    result = search_product(products, "Phone")
    assert result is None

def test_add_product():
    products = [
        {"name": "Laptop", "quantity": 10, "price": 1500},
        {"name": "Monitor", "quantity": 2, "price": 1200},
    ]

    result = add_product(products, "Keyboard", 5, 100)
    assert result is True
    assert len(products) == 3
    assert products[-1]["name"] == "Keyboard"

def test_add_product_duplicate():
    products = [
        {"name": "Laptop", "quantity": 10, "price": 1500},
        {"name": "Monitor", "quantity": 2, "price": 1200},
    ]

    result = add_product(products, "Laptop", 5, 100)
    assert result is False
    assert len(products) == 2

def test_update_quantity():
    products = [
        {"name": "Laptop", "quantity": 10, "price": 1500},
        {"name": "Monitor", "quantity": 2, "price": 1200},
    ]

    result = update_quantity(products, "Laptop", 5)
    assert result is True
    assert products[0]["quantity"] == 15

def test_sell_product():
    products = [
        {"name": "Laptop", "quantity": 10, "price": 1500},
        {"name": "Monitor", "quantity": 2, "price": 1200},   
        ]

    result = sell_product(products, "Laptop", 3)
    assert result is True
    assert products[0]["quantity"] == 7

def test_sell_product_not_enough_stock():
    products = [
        {"name": "Laptop", "quantity": 10, "price": 1500},
        {"name": "Monitor", "quantity": 2, "price": 1200},
    ]

    result = sell_product(products, "Monitor", 5)
    assert result is None
    assert products[1]["quantity"] == 2

def test_sell_product_not_found():
    products = [
        {"name": "Laptop", "quantity": 10, "price": 1500},
        {"name": "Monitor", "quantity": 2, "price": 1200},
    ]

    result = sell_product(products, "Phone", 1)
    assert result is False

def test_delete_product():
    products = [
        {"name": "Laptop", "quantity": 10, "price": 1500},
        {"name": "Monitor", "quantity": 2, "price": 1200}
    ]

    result = delete_product(products, "Laptop")
    assert result is True
    assert len(products) == 1
    assert products[0]["name"] == "Monitor"

def test_delete_product_not_found():
    products = [
        {"name": "Laptop", "quantity": 10, "price": 1500},
        {"name": "Monitor", "quantity": 2, "price": 1200}
    ]

    result = delete_product(products, "Phone")
    assert result is False
    assert len(products) == 2

def test_get_positive_int(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')

    result = get_positive_int('Enter quantity: ')

    assert result == 5

def test_get_positive_int_negative(monkeypatch):
    inputs = iter(["-5", "10"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_positive_int("Enter quantity: ")

    assert result == 10

def test_get_positive_int_invalid_input(monkeypatch):
    inputs = iter(["abc", "10"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_positive_int("Enter quantity: ")

    assert result == 10
