from warehouse import search_product, add_product

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
