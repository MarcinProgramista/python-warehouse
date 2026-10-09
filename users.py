from argon2 import PasswordHasher

password_hasher = PasswordHasher()

SUCCESS = "SUCCESS"
INVALID_EMAIL = "INVALID_EMAIL"
INVALID_PASSWORD = "INVALID_PASSWORD"
EMAIL_ALREADY_EXISTS = "EMAIL_ALREADY_EXISTS"

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
        return INVALID_EMAIL

    if not is_valid_password(password):
        return INVALID_PASSWORD

    if email in users:
        return EMAIL_ALREADY_EXISTS

    users[email] = hash_password(password)
    return SUCCESS

def verify_password(password, hashed_password):
    try:
        return password_hasher.verify(hashed_password, password)
    except Exception:
        return False
