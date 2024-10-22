"""Zip program."""


def main():
    """Zips nuts to bolts."""
    nuts = input("Names [a,b,c]: ").split(",")
    bolts = input("Dates [d/m/y,d/m/y,d/m/y]: ").split(",")
    name_to_date = dict(zip(nuts, bolts))
    print(name_to_date)


main()
