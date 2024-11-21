"""Silver Service (Taxi) Class"""

from prac_09.taxi import Taxi


class SilverService(Taxi):
    """Silver Service (Taxi) Class: fanciness"""
    flagfall = 4.50

    def __init__(self, fanciness=0.0, **kwargs):
        """Construct Silver Service (Taxi) object."""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return taxi string including flag fall."""
        return f"{super().__str__()} plus flag fall of ${self.flagfall:.2f}"

    def get_fare(self):
        """return price for taxi service, including flag fall."""
        return super().get_fare() + self.flagfall
