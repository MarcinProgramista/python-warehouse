
def get_user_products(user_warehouses, email):
    email = email.strip().lower()

    if email not in user_warehouses:
        user_warehouses[email] = []

    return user_warehouses[email]
