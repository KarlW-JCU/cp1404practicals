"""Programming Language Class"""


class ProgrammingLanguage:
    """Programming Language Class: name, typing, reflection, year."""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Construct a programming_language object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return language object summary."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamic."""
        if self.typing == "Dynamic":
            return True
        return False
