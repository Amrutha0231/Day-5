def is_valid_email(email):
    if "@" not in email:
        return False

    local_part, domain_part = email.split("@")

    if not local_part or not domain_part:
        return False

    if "." not in domain_part:
        return False

    return True

def main():
    email = input("Enter an email address: ")

    if is_valid_email(email):
        print("Valid email address!")
    else:
        print("Invalid email address!")

if __name__ == "__main__":
    main()
