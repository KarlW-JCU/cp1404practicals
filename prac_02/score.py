"""
Score checking program
"""

from random import randint


def main():
    score = float(input("Enter score: "))
    print(f"Your score is {determine_performance(score)}.")
    random_score = randint(0, 100)
    print(f"Random score: {random_score} is {determine_performance(random_score)}.")


def determine_performance(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
