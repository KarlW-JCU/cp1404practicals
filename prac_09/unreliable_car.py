"""Unreliable (Car) Class"""

from random import uniform

from prac_09.car import Car


class UnreliableCar(Car):
    """Unreliable (Car) Class: reliability."""

    def __init__(self, reliability=0.0, **kwargs):
        """Construct Unreliable (Car) object."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Drive object given distance if reliability greater than random percentage."""
        if uniform(0, 100) < self.reliability:
            super().drive(distance)
        return distance
