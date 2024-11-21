"""Taxi Simulator Program"""

from taxi import Taxi
from silver_service_taxi import SilverService

MENU = """[C]hoose Taxi
[D]rive
[Q]uit"""
TAXIS = [Taxi(name="Sedan", fuel=50),
         Taxi(name="Maxi", fuel=120),
         SilverService(name="Limo", fuel=200, fanciness=2.0),
         SilverService(name="Hummer", fuel=300, fanciness=4.0)]


def main():
    """"""
    current_taxi = None
    total_trip_cost = 0.0
    print("Let's Drive!")
    print(MENU)
    selection = input(">>> ").upper()
    while selection != "Q":
        try:
            print(f"Current Taxi: {current_taxi.name}")
        except AttributeError:
            pass
        if selection == "C":
            current_taxi = select_taxi(current_taxi)
        elif selection == "D":
            fare = drive_taxi(current_taxi)
            total_trip_cost += fare
        else:
            print("Invalid Option.")
        print(f"Bill to date: ${total_trip_cost:.2f}")
        current_taxi = check_fuel(current_taxi)
        print(MENU)
        selection = input(">>> ").upper()
    print(f"Total trip cost: ${total_trip_cost:.2f}")
    print("Taxis are now:")
    display_taxis()


def select_taxi(current_taxi):
    """Change current taxi to user choice."""
    print("Taxis Available:")
    display_taxis()
    try:
        taxi_number = int(input("Enter your choice: "))
        try:
            return TAXIS[taxi_number]
        except IndexError:
            print("Invalid Taxi Choice.")
    except ValueError:
        print("Invalid Input.")


def drive_taxi(current_taxi):
    """Drive current taxi user defined distance."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive.")
        return 0
    else:
        drive_distance = float(input("Drive how far? "))
        distance_driven = current_taxi.drive(drive_distance)
        print(f"Distance driven: {distance_driven}")
        print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
    return current_taxi.get_fare()


def check_fuel(current_taxi):
    """Return taxi if fuel remaining."""
    try:
        if current_taxi.fuel == 0:
            print("Sorry, Taxi Out of Service.")
            current_taxi = None
    except AttributeError:
        pass
    return current_taxi


def display_taxis():
    """Print each taxi in TAXIS."""
    for i, taxi in enumerate(TAXIS):
        print(f"{i} - {taxi}")


main()
