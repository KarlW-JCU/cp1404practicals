"""
Wimbledon records program.
Estimate: 30 minutes
Actual:   35 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read file and print Wimbledon details."""
    records = read_file(FILENAME)
    champion_to_wins = assign_champion_to_wins(records)
    countries = get_unique_countries(records)
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
    countries = {line[INDEX_COUNTRY] for line in data}
    return countries


def assign_champion_to_wins(data):
    """Return dictionary with champion name to number of wins."""
    champion_to_wins = {}
    for line in data:
        try:
            champion_to_wins[line[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_wins[line[INDEX_CHAMPION]] = 1
    return champion_to_wins


def read_file(file):
    """Return records from file in format: Year,Country,Champion,Country,Runner-up"""
    records = []
    with open(file, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # remove header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
