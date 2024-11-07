"""My Guitar Program"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Display sorted list of guitars, read from file."""
    guitars = load_guitars()
    add_guitar(guitars)
    display_guitars(guitars)
    save_guitars(guitars)


def load_guitars():
    """Return list of guitar objects read from file."""
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


def add_guitar(guitars):
    """Add new guitar/s to guitars from user input."""
    guitar_name = input("Guitar Name: ")
    while guitar_name != "":
        guitar_year = int(input("Guitar Year: "))
        guitar_cost = float(input("Guitar Cost: "))
        new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(new_guitar)
        guitar_name = input("Guitar Name: ")


def display_guitars(guitars):
    """Print sorted list of guitars."""
    for guitar in sorted(guitars):
        print(guitar)


def save_guitars(guitars):
    """Write guitars to file."""
    with open(FILENAME, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
