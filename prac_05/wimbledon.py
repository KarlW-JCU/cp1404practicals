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
    records = load_records(FILENAME)
    champion_to_wins = assign_champion_to_wins(records)
    countries = filter_unique_countries(records)
    display_summary(champion_to_wins, countries)


def display_summary(champion_to_wins, countries):
    """Print summary of champions, number of wins, countries that have won."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(champion, wins)
    print()
    print(f"These {len(countries)} have won Wimbledon:")
    print(", ".join(sorted(countries)))


def filter_unique_countries(data):
    """Return set of unique countries."""
    return {row[INDEX_COUNTRY] for row in data}


def assign_champion_to_wins(data):
    """Return dictionary with champion name to number of wins."""
    champion_to_wins = {}
    for row in data:
        try:
            champion_to_wins[row[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_wins[row[INDEX_CHAMPION]] = 1
    return champion_to_wins


def load_records(file):
    """Return records from file in format: Year,Country,Champion,Country,Runner-up"""
    records = []
    with open(file, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # remove header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
