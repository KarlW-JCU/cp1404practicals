"""
Prize awarding program
Menu driven, get score, print score performance, or print score number of asterisks
(S)core, (R)esult, (P)rize, (Q)uit
"""

MENU = ("(S)core\n"
        "(R)esult\n"
        "(P)rize\n"
        "(Q)uit")


def main():
    """Menu driven, get score, print score performance, print score number of asterisks."""
    score = get_score()
    print(MENU)
    selection = input(">>> ").upper()
    while selection != 'Q':
        if selection == 'S':
            score = get_score()
        elif selection == 'R':
            print(f"A score of {score} is {determine_performance(score)}.")
        elif selection == 'P':
            for i in range(score // 10):
                print("*" * 10)
            print("*" * (score % 10))
        else:
            print("Invalid selection")
        print(MENU)
        selection = input(">>> ").upper()
    print("Farewell")


def get_score():
    """Get numeric score between minimum and maximum thresholds."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100")
        score = int(input("Enter score: "))
    return score


def determine_performance(score):
    """Return threshold-based score performance."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
