import re

def is_strong_password(password):
    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True

def main():
    password = input("Enter a password: ")

    if is_strong_password(password):
        print("Password is strong!")
    else:
        print("Password is weak. Please use a stronger password.")

if __name__ == "__main__":
    main()
