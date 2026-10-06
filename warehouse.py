def show_products(products):
    for product in products:
        print(
            f'Name: {product["name"]}, '
            f'Quantity: {product["quantity"]}, '
            f'Price: {product["price"]}'
        )

def calculate_total_value(products):
    total_value = 0
    for product in products:
        total_value += product["quantity"] * product["price"]
    return total_value

def show_low_stock(products):
    for product in products:
        if product['quantity'] < 5:        
            print(f'Name: {product["name"]}, Quantity:{product["quantity"]}, Price: {product["price"]}')

def find_most_expensive(products):
    product_max_price = 0
    most_expensive = {}
    for product in products:
        if product['price'] > product_max_price:
            product_max_price = product['price']
            most_expensive = product
    return most_expensive

def search_product(products, search_name):
    search_name = search_name.strip()
    for product in products:
        if search_name.lower() in product['name'].lower():
            return product
    return None

def delete_product(products, name):
    product = search_product(products, name)

    if not product:
        return False
    products.remove(product)
    return True

def add_product(products, name, quantity, price):
    validate_quantity(quantity)

    if search_product(products, name):
        return False

    new_product = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    products.append(new_product)
    return True

def update_quantity(products, name, quantity):
    validate_quantity(quantity)

    product = search_product(products, name)

    if product:
        product["quantity"] += quantity
        return True
    return False

def sell_product(products, name, quantity):
    validate_quantity(quantity)

    product = search_product(products, name)
    if not product:
        return False

    if product["quantity"] < quantity:
        return None

    product["quantity"] -= quantity
    return True

def validate_quantity(quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")
