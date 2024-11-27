"""Car class."""


class Car:
    """Car Class: name, fuel."""

    def __init__(self, name="", fuel=0):
        """Construct Car object."""
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def __str__(self):
        """Return car object summary."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

    def __repr__(self):
        """Return developer object summary."""
        return str(vars(self))

    def add_fuel(self, amount):
        """Add amount to object fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive object given distance, or until fuel runs out, then return distance travelled."""
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance
