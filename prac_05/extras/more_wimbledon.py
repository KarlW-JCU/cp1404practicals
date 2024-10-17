"""
Wimbledon champions program.
Estimate: 30 minutes
Actual:   35 minutes
"""

from operator import itemgetter

FILE = "..\\wimbledon.csv"


def main():
    """Print summary of Wimbledon champions and their countries."""
    data = read_file()
    champion_to_wins, champion_to_losses = assign_champion_to_record(data)
    countries = get_unique_countries(data)
    display_summary(champion_to_wins, champion_to_losses, countries)


def display_summary(champion_to_wins, champion_to_losses, countries):
    """Print summary of champions, number of wins, countries that have won."""
    print("Wimbledon Champions:")
    for champion, score in sorted(champion_to_wins.items(), key=itemgetter(1), reverse=True):
        print(champion, score)
    print()
    print(f"These {len(countries)} have won Wimbledon:")
    print(", ".join(countries))
    print()
    print("Wimbledon Losses:")
    for champion, score in sorted(champion_to_losses.items(), key=itemgetter(1), reverse=True):
        print(champion, score)


def get_unique_countries(data):
    """Return set of unique countries."""
    countries = {line.split('"')[0].split(',')[1] for line in data}
    return countries


def assign_champion_to_record(data):
    """Return dictionary with champion name to number of wins and losses."""
    champion_to_wins = {}
    champion_to_losses = {}
    for line in data:
        score_digits = [int(char) for char in line.split('"')[1] if char in '1234567890']
        try:
            champion_to_wins[line.split('"')[0].split(',')[2]] += 1
        except KeyError:
            champion_to_wins[line.split('"')[0].split(',')[2]] = 1
        for i in range(len(score_digits) // 2):
            if (score_digits[i * 2] - score_digits[i * 2 + 1]) < 0:
                try:
                    champion_to_losses[line.split('"')[0].split(',')[2]] += 1
                except KeyError:
                    champion_to_losses[line.split('"')[0].split(',')[2]] = 1
    return champion_to_wins, champion_to_losses


def read_file():
    """Return data from file in format: Year,Country,Champion,Country,Runner-up,Final Scores"""
    with open(FILE, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        data = in_file.read().splitlines()
    return data


main()
