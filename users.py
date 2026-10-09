from argon2 import PasswordHasher
password_hasher = PasswordHasher()

def hash_password(password):
    return password_hasher.hash(password)

def is_valid_email(email):
    email = email.strip()
    
    if email.count("@") != 1:
        return False

    local_part, domain = email.split("@", 1)

    if not local_part or not domain:
        return False

    if "." not in domain:
        return False

    return True

def is_valid_password(password):
    password = password.strip()

    return len(password) >= 12

def normalize_email(email):
    return email.strip().lower()

def register_user(users, email, password):
    email = normalize_email(email)

    if not is_valid_email(email):
        return False

    if not is_valid_password(password):
        return False

    if email in users:
        return False

    users[email] = hash_password(password)
    return True

def verify_password(password, hashed_password):
    try:
        return password_hasher.verify(hashed_password, password)
    except Exception:
        return False
