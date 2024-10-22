"""Address book program."""

MENU = """My Address Book:
[V]iew Addresses
[A]dd Address
[R]emove Address
[S]ave and Quit
"""


def main():
    """Read or update address book on file."""
    name_to_address = read_address_book()
    print(MENU)
    selection = input(">>> ").upper()
    while selection != 'S':
        if selection == 'V':
            display_address_book(name_to_address)
        elif selection == 'A':
            add_new_address(name_to_address)
        elif selection == 'R':
            remove_address(name_to_address)
        else:
            print("Invalid selection.")
        print(MENU)
        selection = input(">>> ").upper()
    save_address_book(name_to_address)


def read_address_book():
    """Read name to address by record from file in format: name,address"""
    with open("addresses.txt", "r") as in_file:
        data = in_file.read().splitlines()
    name_to_address = {record.split(',')[0]: record.split(',')[1] for record in data}
    return name_to_address


def display_address_book(name_to_address):
    """Print name to address by record."""
    max_name_length = max([len(name) for name in name_to_address.keys()])
    print("-" * 20)
    for name, address in name_to_address.items():
        print(f"{name:{max_name_length}}: {address}")
    print("-" * 20)


def add_new_address(name_to_address):
    """Add new name to address record (or update existing name)."""
    name = input("Name: ").title()
    address = input("Address: ")
    name_to_address[name] = address
    print(f"{name} @ {address} added.")


def remove_address(name_to_address):
    """Remove name to address record."""
    name = input("Name: ")
    try:
        name_to_address.pop(name)
        print(f"{name} removed.")
    except KeyError:
        print(f"{name} not in address book.")


def save_address_book(name_to_address):
    """Write name to address by record to file in format: name,address"""
    with open("addresses.txt", "w") as out_file:
        for name, address in sorted(name_to_address.items()):
            print(f"{name},{address}", file=out_file)
    print("Address book saved.")


main()
