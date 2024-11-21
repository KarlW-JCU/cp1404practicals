"""Silver Service (Taxi) Test Program"""

from prac_09.silver_service_taxi import SilverService

my_taxi = SilverService(name="Mercedes", fuel=200, fanciness=2.5)
print(my_taxi)
my_taxi.drive(40)
print(my_taxi, "Fare: $", my_taxi.get_fare())
my_taxi.add_fuel(50)
my_taxi.start_fare()
print(my_taxi)

example = SilverService(name="Hummer", fuel=200, fanciness=4.0)
print(example)
