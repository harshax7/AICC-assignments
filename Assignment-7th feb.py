import re
import hashlib
import getpass

# Function to check password strength
def is_strong_password(password):
    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return True
    return False

# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Registration
print("=== Create Account ===")
while True:
    password = getpass.getpass("Create a strong password: ")
    
    if is_strong_password(password):
        confirm = getpass.getpass("Confirm password: ")
        if password == confirm:
            stored_password = hash_password(password)
            print("Account created successfully!\n")
            break
        else:
            print("Passwords do not match. Try again.\n")
    else:
        print("Weak password! Must contain:")
        print("- At least 8 characters")
        print("- Uppercase, lowercase")
        print("- Number")
        print("- Special character\n")

# Login System
print("=== Login ===")
attempts = 3

while attempts > 0:
    entered_password = getpass.getpass("Enter password: ")
    
    if hash_password(entered_password) == stored_password:
        print("Login successful! ✅")
        break
    else:
        attempts -= 1
        print(f"Incorrect password! Attempts left: {attempts}")

if attempts == 0:
    print("Account locked! ❌ Too many failed attempts.")