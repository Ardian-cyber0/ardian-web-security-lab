import json
import hashlib
import secrets
import getpass

USERNAME = input("Username: ")
PASSWORD = getpass.getpass("Password: ")

salt = secrets.token_hex(16)

password_hash = hashlib.sha256(
    (salt + PASSWORD).encode()
).hexdigest()

try:
    with open("users.json", "r") as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}

users[USERNAME] = {
    "salt": salt,
    "password_hash": password_hash
}

with open("users.json", "w") as f:
    json.dump(users, f, indent=4)

print("\nUser berhasil dibuat.")
print(f"Username: {USERNAME}")
print(f"Salt: {salt}")
print(f"Password hash: {password_hash}")
