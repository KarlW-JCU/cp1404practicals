"""Wimbledon champions program."""

from operator import itemgetter

FILE = "..\\wimbledon.csv"
MENU = """Wimbledon Records.
[1]Champions!
[2]Finals Losses.
[3]Countries.
[9]Summary.
[0]Exit."""


def main():
    """Print selected summaries of Wimbledon champions and their countries."""
    data = read_file()
    champion_to_wins = assign_champion_to_wins(data)
    champion_to_losses = assign_champion_to_losses(data)
    countries = count_countries(data)
    print(MENU)
    selection = input(">>> ")
    while selection != "0":
        if selection == "1":
            display_champions(champion_to_wins)
        elif selection == "2":
            display_losses(champion_to_losses)
        elif selection == "3":
            display_countries(countries)
        elif selection == "9":
            display_champions(champion_to_wins)
            display_losses(champion_to_losses)
            display_countries(countries)
        else:
            print("Invalid selection.")
        print(MENU)
        selection = input(">>> ")


def display_countries(countries):
    """Display sorted list of countries by number of finalists."""
    print(f"These {len(countries)} have won Wimbledon:")
    for country, number_of_players in sorted(countries.items(), key=itemgetter(1), reverse=True):
        print(f"{country}:{number_of_players}", end="; ")
    print()
    print("-" * 20)


def display_losses(champion_to_losses):
    """Print sorted list of game losses."""
    print("Wimbledon Finals Losses:")
    for champion, score in sorted(champion_to_losses.items(), key=itemgetter(1), reverse=True):
        print(champion, score)
    print("-" * 20)


def display_champions(champion_to_wins):
    """Print sorted list table of champions."""
    print("Wimbledon Champions:")
    for champion, score in sorted(champion_to_wins.items(), key=itemgetter(1), reverse=True):
        print(champion, score)
    print("-" * 20)


def count_countries(data):
    """Return set of unique countries."""
    countries = {}
    for line in data:
        for country in [line.split('"')[0].split(',')[1], line.split('"')[0].split(',')[3]]:
            try:
                countries[country] += 1
            except KeyError:
                countries[country] = 1
    return countries


def assign_champion_to_wins(data):
    """Return dictionary with champion name to number of wins."""
    champion_to_wins = {}
    for line in data:
        try:
            champion_to_wins[line.split('"')[0].split(',')[2]] += 1
        except KeyError:
            champion_to_wins[line.split('"')[0].split(',')[2]] = 1
    return champion_to_wins


def assign_champion_to_losses(data):
    """Return dictionary with champion name to number of losses."""
    champion_to_losses = {}
    for line in data:
        score_digits = [int(char) for char in line.split('"')[1] if char in '1234567890']
        for i in range(len(score_digits) // 2):
            if (score_digits[i * 2] - score_digits[i * 2 + 1]) < 0:
                try:
                    champion_to_losses[line.split('"')[0].split(',')[2]] += 1
                except KeyError:
                    champion_to_losses[line.split('"')[0].split(',')[2]] = 1
    return champion_to_losses


def read_file():
    """Return data from file in format: Year,Country,Champion,Country,Runner-up,Final Scores"""
    with open(FILE, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        data = in_file.read().splitlines()
    return data


main()
