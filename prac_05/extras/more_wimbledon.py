"""
Wimbledon champions program.
Estimate: 30 minutes
Actual:   35 minutes
"""

FILE = "..\\wimbledon.csv"


def main():
    """Print summary of Wimbledon champions and their countries."""
    data = read_file()
    champion_to_wins = assign_champion_to_wins(data)
    countries = get_unique_countries(data)
    display_summary(champion_to_wins, countries)


def display_summary(champion_to_wins, countries):
    """Print summary of champions, number of wins, countries that have won."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(champion, wins)
    print()
    print(f"These {len(countries)} have won Wimbledon:")
    print(", ".join(countries))


def get_unique_countries(data):
    """Return set of unique countries."""
    countries = {line.split('"')[0].split(',')[1] for line in data}
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


def read_file():
    """Return data from file in format: Year,Country,Champion,Country,Runner-up,Final Scores"""
    with open(FILE, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        data = in_file.read().splitlines()
    return data


main()
