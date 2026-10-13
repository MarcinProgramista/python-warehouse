from user_warehouse import get_user_products
from warehouse import add_product

def test_get_user_products_creates_empty_warehouse():
    user_warehouses = {}

    products = get_user_products(
        user_warehouses,
        "marcin@example.com"
    )

    assert products == []
    assert "marcin@example.com" in user_warehouses

def test_users_have_separate_warehouses():
    user_warehouses = {}

    marcins_products = get_user_products(
        user_warehouses,
        "marcin@example.com"
    )

    annas_products = get_user_products(
        user_warehouses,
        "anna@example.com"
    )

    marcins_products.append({
        "name": "Laptop",
        "quantity": 1,
        "price": 3000
    })

    assert len(marcins_products) == 1
    assert annas_products == []
    assert marcins_products is not annas_products

def test_get_user_products_normalizes_email():
    user_warehouses = {}

    first_products = get_user_products(
        user_warehouses,
        "marcin@example.com"
    )

    second_products = get_user_products(
        user_warehouses,
        " MARCIN@EXAMPLE.COM "
    )

    first_products.append({
        "name": "Laptop",
        "quantity": 1,
        "price": 3000
    })

    assert second_products == first_products
    assert len(user_warehouses) == 1


def test_adding_product_affects_only_one_user():
    user_warehouses = {}

    marcins_products = get_user_products(
        user_warehouses,
        "marcin@example.com"
    )
    annas_products = get_user_products(
        user_warehouses,
        "anna@example.com"
    )

    result = add_product(
        marcins_products,
        "Laptop",
        1,
        3000
    )

    assert result is True
    assert len(marcins_products) == 1
    assert annas_products == []
