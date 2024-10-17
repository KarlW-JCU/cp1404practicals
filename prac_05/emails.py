"""
Email program.
Estimate: 30 minutes
Actual:   15 minutes
"""

name_to_email = {}
email = input("Email: ")
while email != '':
    name = email.split('@')[0].replace('.', ' ').replace('_', ' ').title()
    confirm = input(f"Is your name {name}? (Y/n) ").upper()
    if confirm == '':
        confirm = 'Y'
    if confirm != 'Y':
        name = input("Name: ")
    name_to_email[name] = email
    email = input("Email: ")

for name, email in name_to_email.items():
    print(f"{name} ({email})")
