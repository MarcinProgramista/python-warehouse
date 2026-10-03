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

def delete_product(products):
    name = input('Enter product name to delete: ')
    product = search_product(products, name)

    if product:
        products.remove(product)
        print(f'Product "{product["name"]}" deleted.')
    else:
        print('Product not found.')