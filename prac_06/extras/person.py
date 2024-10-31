"""Person Class Program"""


class Person:
    """Person class: first_name, last_name, age"""

    def __init__(self, first_name="", last_name="", age=0):
        """Construct person object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.age})"

    def __repr__(self):
        return f"{vars(self)}"


if __name__ == "__main__":
    print(Person("Bob", "Saggit", 42))
    print(repr(Person("Bob", "Saggit", 42)))
