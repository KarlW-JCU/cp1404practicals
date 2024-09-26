"""
Prize awarding program
"""

MENU = ("(S)core\n"
        "(R)esult\n"
        "(P)rize\n"
        "(Q)uit")


def main():
    score = get_score()
    print(MENU)
    selection = input(">>> ").upper()
    while selection != 'Q':
        if selection == 'S':
            score = get_score()
        elif selection == 'R':
            print(f"A score of {score} is {determine_performance(score)}.")
        elif selection == 'P':
            print("*" * score)
        else:
            print("Invalid selection")
        print(MENU)
        selection = input(">>> ").upper()
    print("Farewell")


def get_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100")
        score = int(input("Enter score: "))
    return score


def determine_performance(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
