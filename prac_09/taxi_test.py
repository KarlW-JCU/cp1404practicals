"""Taxi (Car) Test Program"""
from prac_09.taxi import Taxi

my_taxi = Taxi(name="Prius 1", fuel=100)
my_taxi.drive(40)
print(my_taxi)
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi, my_taxi.current_fare_distance)
