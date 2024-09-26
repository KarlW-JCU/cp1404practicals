"""
Simple password program
Get a password with minimum length and display asterisks of password length
"""

MINIMUM_LENGTH = 8


def main():
    """Get and print password in asterisks."""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get password of valid minimum length."""
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters long.")
        password = input("Password: ")
    return password


def print_asterisks(string):
    """Print length of string number of asterisks."""
    print("Password: ", "*" * len(string), sep='')


main()
