"""Simple ASCII convertor."""

MENU = ("[1]ASCII to Value\n"
        "[2]Value to ASCII\n"
        "[3]ASCII Table\n"
        "[Q]uit")
CHARACTER_LIMIT = (33, 126)


def main():
    """Simple ASCII convertor."""
    print(MENU)
    selection = input("Selection: ").upper()
    while selection != 'Q':
        if selection == '1':
            character = input("Enter a character: ")
            print_ascii(character)
        elif selection == '2':
            try:
                value = int(input(f"Enter a number between {CHARACTER_LIMIT[0]} and {CHARACTER_LIMIT[1]}: "))
            except ValueError:
                print("Invalid input: Non Integer.")
            else:
                print_character(value)
        elif selection == '3':
            print_ascii_table()
        else:
            print("Invalid selection.")
        print(MENU)
        selection = input("Selection: ").upper()
    print("Goodbye :)")


def print_ascii(character):
    if len(character) == 1:
        print(f"The ASCII code for {character} is: {ord(character)}")
    else:
        print("Invalid character.")


def print_character(value):
    if value < CHARACTER_LIMIT[0] or value > CHARACTER_LIMIT[1]:
        print("Invalid value.")
    else:
        print(f"The character for {value} is: {chr(value)}")


def print_ascii_table():
    for i in range(CHARACTER_LIMIT[0], CHARACTER_LIMIT[1] + 1):
        print(f"{i:>3} {chr(i)}")


main()
