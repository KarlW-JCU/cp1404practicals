"""Unreliable (Car) Test Program"""

from prac_09.unreliable_car import UnreliableCar

old_car = UnreliableCar(name="Toyota", fuel=200, reliability=33.33)
new_car = UnreliableCar(name="Mitsubishi", fuel=200, reliability=100.00)
for i in range(10):
    old_car.drive(20)
    new_car.drive(20)
print(old_car)
print(new_car)
