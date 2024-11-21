"""Unreliable (Car) Test Program"""
from prac_09.unreliable_car import UnreliableCar

my_car = UnreliableCar(name="Toyota", fuel=100, reliability=66.66)
my_car.drive(20)
print(my_car)
my_car.drive(20)
print(my_car)
my_car.drive(20)
print(my_car)
my_car.drive(20)
print(my_car)
my_car.drive(20)
print(my_car)
my_car.add_fuel(50)
print(my_car)
