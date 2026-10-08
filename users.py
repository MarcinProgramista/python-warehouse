def register_user(users, username, password):
    if username in users:
        return False

    users[username] = password
    return True
