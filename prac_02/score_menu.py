"""
Prize awarding program
"""

MENU = ("(S)core\n"
        "(R)esult\n"
        "(P)rize\n"
        "(Q)uit\n")


def main():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100")
        score = int(input("Enter score: "))
    print(MENU)
    selection = input(">>> ").upper()
    while selection != 'Q':
        if selection == 'S':
            pass
        elif selection == 'R':
            pass
        elif selection == 'P':
            pass
        else:
            print("Invalid selection")
        print(MENU)
        selection = input(">>> ").upper()
    print("Farewell")


main()
