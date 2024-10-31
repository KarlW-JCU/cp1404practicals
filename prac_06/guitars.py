"""Guitars Program"""

from prac_06.guitar import Guitar

guitars = []
print("My Guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.\n")
    name = input("Name: ")

# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
# guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

print("\nThese are my guitars:")
max_name_length = max(len(guitar.name) for guitar in guitars)
max_price_length = max(len(str(guitar.cost)) for guitar in guitars)
for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(
        f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:{max_price_length + 2},.2f} {vintage_string}")
