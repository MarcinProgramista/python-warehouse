from utils import get_positive_int, get_positive_float
import warehouse
warehouse_name = "MY WAREHOUSE"
products = [
    {"name": "Laptop", "quantity": 5, "price": 3000},
    {"name": "Monitor", "quantity": 2, "price": 1200},
    {"name": "Mysz", "quantity": 20, "price": 80},
    {"name": "Klawiatura", "quantity": 0, "price": 150}
]
def show_menu(warehouse_name):
    print('========================')
    print(f'     {warehouse_name}      ')
    print('========================')
    print('1. Show products')
    print('2. Total warehouse value')
    print('3. Low stock')
    print('4. Most expensive product')
    print('5. Search product')
    print('6. Add product')
    print('7. Update quantity')
    print('8. Sell product')
    print('9. Delete product')
    print('0. Exit')

def handle_choice(choice, products):
    if choice == '1':
        warehouse.show_products(products)
    elif choice == '2':
        total_value = warehouse.calculate_total_value(products)
        print(f'Total warehouse value: {total_value} zł')
    elif choice == '3':
        warehouse.show_low_stock(products)
    elif choice == '4':
        most_expensive = warehouse.find_most_expensive(products)
        print(
            f'Most expensive: '
            f'{most_expensive["name"]} - '
            f'{most_expensive["price"]} zł'
            )
    elif choice == '5':
        search_name = input('Enter product name to search: ')
        found_product = warehouse.search_product(products, search_name)

        if found_product:
            print(
            f'Product found: '
            f'{found_product["name"]} - '
            f'{found_product["price"]} zł'
            )
        else:
            print('Product not found.')
        
    elif choice == '6':
        add_product_menu(products)
    elif choice == '7':
        update_quantity(products)
    elif choice == '8':
        sell_product(products)  
    elif choice == '9':
        warehouse.delete_product(products)
    else:
        print('Invalid option.')

def add_product_menu(products):
    name = input('Enter product name: ')
    quantity = get_positive_int('Enter quantity: ')
    price = get_positive_float('Enter price: ')
   
    if warehouse.add_product(products, name, quantity, price):
        print('Product added successfully.')
    else:
        print('Product already exists.')
def update_quantity(products):
    name = input('Enter product name: ')
    new_quantity = get_positive_int('Enter quantity: ')
    product = warehouse.search_product(products, name)
    if product:
        product["quantity"] = new_quantity + product["quantity"]
    else:
        print('Product not found.')
def sell_product(products):
    name = input('Enter product name: ')
    quantity_to_sell = get_positive_int('Enter quantity: ')
    product = warehouse.search_product(products, name)

    if product:
        if product["quantity"] >= quantity_to_sell:
            product["quantity"] -= quantity_to_sell
            print(f'Sold {quantity_to_sell} of {product["name"]}.')
        else:
            print('Not enough stock to sell.')
    else:
        print('Product not found.')                                                                                                                                                                                                                                                                                  
while True:
    show_menu(warehouse_name)
    choice = input('Choose an option: ')
   
    if choice == '0':
            print('Goodbye!')
            break
    
    handle_choice(choice, products)