import hashlib
import os

def hash_password(password):
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + hashed_password

def check_password(password, hashed_password):
    salt = hashed_password[:16]
    new_hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return hashed_password == salt + new_hashed_password

# Example usage
password = "my_password"

# Hash the password
hashed_password = hash_password(password)
# Check if a password matches the stored hash
is_password_match = check_password("my_password", hashed_password)

print("Password match:", is_password_match)
