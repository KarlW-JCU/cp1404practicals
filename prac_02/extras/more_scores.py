"""
Random score generating/recording program
"""

from random import randint


def main():
    scores = []
    number_of_scores = int(input("Number of scores: "))
    for i in range(number_of_scores):
        scores.append(randint(0, 100))
    file_out = open("results.txt", "w")
    for score in scores:
        print(f"{score} is {determine_performance(score)}", file=file_out)
    file_out.close()
    print("Done.")


def determine_performance(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
