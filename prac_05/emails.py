"""
Email program.
Estimate: 30 minutes
Actual:   15 minutes
"""


def main():
    """Create dictionary of name_to_email."""
    name_to_email = {}
    email = input("Email: ")
    while email != '':
        name = get_name_from_email(email)
        confirm = input(f"Is your name {name}? (Y/n) ").upper()
        if confirm != '' and confirm != 'Y':
            name = input("Name: ")
        name_to_email[name] = email
        email = input("Email: ")

    for name, email in name_to_email.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Return name from email address."""
    name = email.split('@')[0].replace('.', ' ').replace('_', ' ').title()

    return name


main()
