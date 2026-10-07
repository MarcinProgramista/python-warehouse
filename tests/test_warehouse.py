import pytest
from warehouse import (
    search_product,
    add_product,
    update_quantity,
    sell_product,
    delete_product,
    validate_quantity,
    calculate_total_value,
    find_most_expensive,
    show_low_stock,
    show_products,
)
from utils import get_positive_int, get_positive_float

def test_search_product_found(products):
    result = search_product(products, "Laptop")

    assert result["name"] == "Laptop"

def test_search_product_not_found(products):
    result = search_product(products, "Phone")

    assert result is None

def test_add_product(products):
    result = add_product(products, "Keyboard", 5, 100)

    assert result is True
    assert len(products) == 3
    assert products[-1]["name"] == "Keyboard"

def test_add_product_duplicate(products):
    result = add_product(products, "Laptop", 5, 100)

    assert result is False
    assert len(products) == 2

def test_update_quantity(products):
    result = update_quantity(products, "Laptop", 5)

    assert result is True
    assert products[0]["quantity"] == 15

def test_sell_product(products):
    result = sell_product(products, "Laptop", 3)
    assert result is True
    assert products[0]["quantity"] == 7

def test_sell_product_not_enough_stock(products):
    result = sell_product(products, "Monitor", 5)

    assert result is None
    assert products[1]["quantity"] == 2

def test_sell_product_not_found(products):
    result = sell_product(products, "Phone", 1)

    assert result is False

def test_delete_product(products):
    result = delete_product(products, "Laptop")

    assert result is True
    assert len(products) == 1
    assert products[0]["name"] == "Monitor"

def test_delete_product_not_found(products):
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

def test_get_positive_float(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: '12.5')

    result = get_positive_float('Enter price:')

    assert result == 12.5

def test_get_positive_float_negative(monkeypatch):
    inputs = iter(["-5.5", "10.5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_positive_float("Enter price: ")

    assert result == 10.5

def test_get_positive_float_invalid_input(monkeypatch):
    inputs = iter(["abc", "10.5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_positive_float("Enter price: ")

    assert result == 10.5

@pytest.mark.parametrize("name, quantity, price, expected",
    [
        ("Keyboard", 5, 100, True),
        ("Mouse", 10, 50, True),
        ("Printer", 2, 800, True),
    ]
)
def test_add_product_parametrized(products, name, quantity, price, expected):
    result = add_product(products, name, quantity, price)

    assert result == expected
    assert products[-1]["name"] == name

@pytest.mark.parametrize(
    "name, quantity, price",
    [
        ("Laptop", 5, 100),
        ("Monitor", 10, 50)
    ]
)
def test_add_product_duplicate_parametrized(products, name, quantity, price):
    result = add_product(products, name, quantity, price)

    assert result is False
    assert len(products) == 2

def test_add_product_negative_quantity(products):
    with pytest.raises(ValueError):
        add_product(products, "Keyboard", -5, 100)

def test_invalid_int():
    with pytest.raises(ValueError):
        int("abc")

def test_invalid_quantity():
    with pytest.raises(ValueError):
        int("-abc")

def test_validate_quantity_valid():
    result = validate_quantity(10)

    assert result is None

def test_validate_quantity_negative():
    with pytest.raises(ValueError):
        validate_quantity(-5)

def test_update_quantity_negative(products):
    with pytest.raises(ValueError):
        update_quantity(products, "Laptop", -5)

def test_sell_product_negative(products):
    with pytest.raises(ValueError):
        sell_product(products, "Laptop", -5)

def test_update_quantity_not_found(products):
    result = update_quantity(products, "Phone", 5)

    assert result is False

def test_calculate_total_value(products):
    result = calculate_total_value(products)

    assert result == 17400

def test_find_most_expensive(products):
    result = find_most_expensive(products)

    assert result["name"] == "Laptop"
    assert result["price"] == 1500

def test_show_low_stock(products, capsys):
    show_low_stock(products)

    captured = capsys.readouterr()

    assert "Monitor" in captured.out
    assert "Laptop" not in captured.out

def test_show_products(products, capsys):
    show_products(products)

    captured = capsys.readouterr()

    assert "Laptop" in captured.out
    assert "Monitor" in captured.out
