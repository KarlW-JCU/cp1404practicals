"""
1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program
"""

MENU_STRING = ("[N]ew Numbers\n"
               "[E]vens\n"
               "[O]dds\n"
               "[S]quares\n"
               "[Q]uit")


def main():
    range_min = 0
    range_max = 0
    print("Learning numbers is fun!")
    print(MENU_STRING)
    selection = input(">>> ").upper()
    while selection != "Q":
        while range_min == range_max == 0:
            print("Select two numbers first :)")
            range_min, range_max = select_numbers()
            selection = ''
        while range_min >= range_max:
            print("The second number must be larger than the first number :)")
            range_min, range_max = select_numbers()
            selection = ''
        if selection == "N":
            print("Choose new numbers :)")
            range_min, range_max = select_numbers()
        elif selection == "E":
            print("Even numbers in your number range.")
            for i in range(range_min, range_max + 1):
                if i % 2 == 0:
                    print(i, end=' ')
            print()
        elif selection == "O":
            print("Odds numbers in your number range.")
            for i in range(range_min, range_max + 1):
                if i % 2 != 0:
                    print(i, end=' ')
            print()
        elif selection == "S":
            print("Squared numbers in your number range.")
            for i in range(range_min, range_max + 1):
                print(i ** 2, end=' ')
            print()
        print(MENU_STRING)
        print(f"Your numbers: {range_min} and {range_max}")
        selection = input(">>> ").upper()
    print("Goodbye :)")


def select_numbers():
    range_min = int(input("Enter your first number : "))
    range_max = int(input("Enter your second number: "))
    return range_min, range_max


main()
