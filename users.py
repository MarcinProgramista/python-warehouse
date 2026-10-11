from argon2 import PasswordHasher
from argon2.exceptions import (
    VerificationError,
    InvalidHashError,
)

password_hasher = PasswordHasher()

SUCCESS = "SUCCESS"
INVALID_EMAIL = "INVALID_EMAIL"
INVALID_PASSWORD = "INVALID_PASSWORD"
EMAIL_ALREADY_EXISTS = "EMAIL_ALREADY_EXISTS"
INVALID_CREDENTIALS = "INVALID_CREDENTIALS"

def change_password(users, email, old_password, new_password):
    email = normalize_email(email)

    if email not in users:
        return INVALID_CREDENTIALS

    if not verify_password(old_password, users[email]):
        return INVALID_CREDENTIALS

    if not is_valid_password(new_password):
        return INVALID_PASSWORD

    users[email] = hash_password(new_password)

    return SUCCESS

def login_user(users, email, password):
    email = normalize_email(email)

    if email not in users:
        return INVALID_CREDENTIALS
    if not verify_password(password, users[email]):
        return INVALID_CREDENTIALS

    return SUCCESS

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
    except(VerificationError, InvalidHashError) :
        return False
