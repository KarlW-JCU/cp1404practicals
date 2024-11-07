"""Guitar Class Program"""

CURRENT_YEAR = 2024
VINTAGE_AGE = 50


class Guitar:
    """Guitar class: name, year, cost."""

    def __init__(self, name="", year=0, cost=0.0):
        """Construct guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return guitar object summary."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def __repr__(self):
        """Return developer object summary."""
        return f"{vars(self)}"

    def __lt__(self, other):
        """Determine if guitar year is less than other guitar year."""
        return self.year < other.year

    def calculate_age(self):
        """Return guitar age based on CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage."""
        return self.calculate_age() > VINTAGE_AGE


if __name__ == "__main__":
    test_guitar = Guitar("Test", 1992, 12345.95)
    second_guitar = Guitar("Second", 2020, 699.99)
    print(test_guitar)
    print(repr(test_guitar))
    print(test_guitar.calculate_age())
    print(test_guitar.is_vintage())
    print(test_guitar < second_guitar)
