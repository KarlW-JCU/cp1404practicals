"""
Automatic Password Generator Program.
"""

import random

MIN_LENGTH = 8
MAX_LENGTH = 16
IS_SPECIAL_CHARACTER_REQUIRED = True
NUMBERS = "0123456789"
LETTERS = "abcdefghijklmnopqrstuvwxyz"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to generate, check, and print a password."""
    print("Generating Password...")
    print(f"Your password will be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    word_length = random.randint(MIN_LENGTH, MAX_LENGTH)
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters:", SPECIAL_CHARACTERS)
    input("Press 'Enter' to continue...")
    password = generate_password(word_length)
    while not is_valid_password(password):
        password = generate_password(word_length)
    print(f"Your {len(password)}-character password is: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1
        else:
            return False
    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False
    return True


def generate_password(word_length):
    """Generate a random password."""
    word = ""
    for character in range(word_length):
        random_character = random.random()
        if random_character <= 0.25:
            word += random.choice(LETTERS).upper()
        elif random_character <= 0.50:
            word += random.choice(LETTERS)
        elif random_character <= 0.75:
            word += random.choice(NUMBERS)
        else:
            word += random.choice(SPECIAL_CHARACTERS)
    return word


main()
