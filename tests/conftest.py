import pytest


@pytest.fixture
def products():
    return [
        {"name": "Laptop", "quantity": 10, "price": 1500},
        {"name": "Monitor", "quantity": 2, "price": 1200},
    ]
