"""Car Simulator Program."""

from prac_06.car import Car

MENU = """Menu:
d) drive
r) refuel
q) quit"""


def main():
    """Car driving simulator."""
    print("Let's Drive!")
    car = create_car()
    print(car)
    print(MENU)
    selection = input("Enter your choice: ").upper()
    while selection != "Q":
        if selection == "D":
            drive_car(car)
        elif selection == "R":
            refuel_car(car)
        else:
            print("Invalid Selection.")
        print(car)
        print(MENU)
        selection = input("Enter your choice: ").upper()
    print(f"Good Bye, {car.name}'s driver :)")


def create_car():
    """Create car object with user defined name."""
    car_name = input("Enter your care name: ")
    while car_name == "":
        car_name = input("Enter your care name: ")
    return Car(car_name, 100)


def drive_car(car):
    """Drive car up to user define distance or maximum fuel allowance."""
    try:
        drive = int(input("How many km do you wish to drive? "))
        while drive < 0:
            print("Distance must be >= 0")
            drive = int(input("How many km do you wish to drive? "))
        distance = car.drive(drive)
        fuel_message = ", and ran out of fuel." if car.fuel == 0 else "."
        print(f"The car drove {distance}km{fuel_message}")
    except ValueError:
        print("Error: Not a number.")


def refuel_car(car):
    """Add user defined units of fuel."""
    try:
        fuel = int(input("How many units of fuel do you want to add to the car? "))
        while fuel < 0:
            print("Fuel amount must be >= 0")
            fuel = int(input("How many units of fuel do you want to add to the car? "))
        car.add_fuel(fuel)
        print(f"Added {fuel} units of fuel.")
    except ValueError:
        print("Error: Not a number.")


main()
