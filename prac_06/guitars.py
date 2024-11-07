"""Guitars Program"""

from prac_06.guitar import Guitar


def main():
    """Guitar record program."""
    guitars = []
    print("My Guitars!")
    add_guitar(guitars)
    # add_test_objects(guitars)
    if guitars:
        display_guitars(guitars)
    else:
        print("I do not own any guitars :(")


def add_guitar(guitars):
    """Add new guitar/s to guitars."""
    name = input("Name: ")
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"{new_guitar} added.\n")
        except ValueError:
            print("Invalid input: Start again.")
        name = input("Name: ")


def add_test_objects(guitars):
    """Add test objects to guitars."""
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))


def display_guitars(guitars):
    """Print formatted list of guitars."""
    print("\nThese are my guitars:")
    max_name_length = max(len(guitar.name) for guitar in guitars)
    max_price_length = max(len(str(guitar.cost)) for guitar in guitars)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), "
            f"worth ${guitar.cost:{max_price_length + 2},.2f} {vintage_string}")


main()
