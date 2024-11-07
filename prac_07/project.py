"""Project Class Program"""


class Project:
    """Project Class: name, start_date, priority, cost_estimate, completion_percentage"""

    def __init__(self, name="", start_date="00/00/00", priority=0,
                 cost_estimate=0.0, completion_percentage=0.0):
        """Construct Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return project object summary."""
        return (f"{self.name}, Started: {self.start_date}, Priority: {self.priority}, "
                f"Estimated Cost: ${self.cost_estimate:.2f}, Completion Percentage: {self.completion_percentage}%")

    def __repr__(self):
        """Return developer object summary."""
        return f"{vars(self)}"


if __name__ == "__main__":
    test = Project("Build", "1/10/2020", 0, 12345.95, 42.5)
    print(test)
    print(repr(test))
