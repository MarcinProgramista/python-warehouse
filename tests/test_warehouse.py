from warehouse import search_product

def test_search_product_found():
    products = [
        {"name": "Laptop", "quantity": 10, "price": 1500},
        {"name": "Monitor", "quantity": 2, "price": 1200},
    ]

    result = search_product(products, "Laptop")
    assert result["name"] == "Laptop"
