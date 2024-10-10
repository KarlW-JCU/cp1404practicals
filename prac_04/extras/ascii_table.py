"""ASCII program."""

MENU = ("[0]ASCII Range\n"
        "[1]ASCII to Value\n"
        "[2]Value to ASCII\n"
        "[3]ASCII Table\n"
        "[Q]uit")
CHARACTER_LIMIT = (33, 126)


def main():
    """Simple ASCII convertor."""
    lower, upper = CHARACTER_LIMIT
    print(MENU)
    selection = input("Selection: ").upper()
    while selection != 'Q':
        if selection == '0':
            lower, upper = get_number()
        elif selection == '1':
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
            try:
                number_of_columns = int(input("Table columns: "))
            except ValueError:
                print("Invalid input: Non Integer.")
            else:
                print_ascii_table(number_of_columns, lower, upper)
        else:
            print("Invalid selection.")
        print(MENU)
        selection = input("Selection: ").upper()
    print("Goodbye :)")


def get_number():
    is_valid = False
    while not is_valid:
        try:
            lower = int(input(f"Enter lower number (>= {CHARACTER_LIMIT[0]}): "))
            while lower < CHARACTER_LIMIT[0]:
                print("Invalid value.")
                lower = int(input(f"Enter lower number (>= {CHARACTER_LIMIT[0]}): "))
            upper = int(input(f"Enter upper number ({lower} < upper <= {CHARACTER_LIMIT[1]}): "))
            while lower > upper or upper > CHARACTER_LIMIT[1]:
                print("Invalid value: upper < lower.")
                upper = int(input(f"Enter upper number ({lower} < upper <= {CHARACTER_LIMIT[1]}): "))
            is_valid = True
        except ValueError:
            print("Invalid input: Non Integer.")
    return lower, upper


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


def print_ascii_table(number_of_columns, lower, upper):
    column_limit = (upper - lower) // number_of_columns + 1
    for i in range(lower, lower + column_limit):
        for j in range(0, number_of_columns):
            if i + j * column_limit <= upper:
                print(f"{i + j * column_limit:>3} {chr(i + j * column_limit)} ", end="")
        print()


main()
