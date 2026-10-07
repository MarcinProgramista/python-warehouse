import pytest
from utils import get_positive_int, get_positive_float

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
