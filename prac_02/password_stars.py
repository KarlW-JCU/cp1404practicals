"""
Simple password program
"""

MIN_LENGTH = 8


def main():
    password = get_password()
    print_stars(password)


def get_password():
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Password: ")
    return password


def print_stars(string):
    print("Password: ", "*" * len(string), sep='')


main()
