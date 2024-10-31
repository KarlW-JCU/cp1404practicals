"""Guitar Class Program"""

CURRENT_YEAR = 2024

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

    def get_age(self):
        """Return guitar object age."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar object is vintage."""
        return self.get_age() > 50


if __name__ == "__main__":
    test_guitar = Guitar("Test", 1992, 12345.95)
    print(test_guitar)
    print(test_guitar.get_age())
    print(test_guitar.is_vintage())
