"""Date class program."""


class Date:
    """Date class: day, month, year"""

    def __init__(self, day=0, month=0, year=0):
        """Construct date object."""
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """Return date object summary."""
        return "{}/{}/{}".format(self.day, self.month, self.year)

    def __repr__(self):
        """Return developer date object summary."""
        return f"{vars(self)}"

    def add_days(self, days):
        """Add days to date object."""
        if self.month == 2:
            if self.year % 4 == 0 and self.day + days > 29:
                self.day += days - 29
                self.month += 1
            elif self.day + days > 28:
                self.day += days - 28
                self.month += 1
            else:
                self.day += days
        elif self.month in [4, 6, 9, 11]:
            if self.day + days > 30:
                self.day += days - 30
                self.month += 1
            else:
                self.day += days
        elif self.month in [1, 3, 5, 7, 8, 10]:
            if self.day + days > 31:
                self.day += days - 31
                self.month += 1
            else:
                self.day += days
        else:
            if self.day + days > 31:
                self.day += days - 31
                self.month = 1
                self.year += 1
            else:
                self.day += days


if __name__ == "__main__":
    birth = Date(13, 12, 1992)
    print(birth)
    birth.add_days(18)
    print(birth)
    birth.add_days(1)
    print(birth)
