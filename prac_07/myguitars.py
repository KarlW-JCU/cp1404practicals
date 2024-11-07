"""My Guitar Program"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Display sorted list of guitars, read from file."""
    guitars = load_guitars()
    display_guitars(guitars)


def load_guitars():
    """Return list of guitars from file."""
    guitars = []
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar_name = parts[0]
            guitar_year = int(parts[1])
            guitar_cost = float(parts[2])
            new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
            guitars.append(new_guitar)
    return guitars


def display_guitars(guitars):
    """Print sorted list of guitars."""
    for guitar in sorted(guitars):
        print(guitar)


main()
