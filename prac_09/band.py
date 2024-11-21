"""Band Class Program"""


class Band():
    """Band Class: name"""

    def __init__(self, name=""):
        """Construct band class object."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of band."""
        band_musicians = ""
        for musician in self.musicians:
            band_musicians += f"{musician}, "
        return f"{self.name} ({band_musicians.rstrip(", ")})"

    def __repr__(self):
        """Return developer string representation of object."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """"""
        play_string = ""
        for musician in self.musicians:
            play_string += f"{musician.play()}\n"
        return play_string.strip()


if __name__ == "__main__":
    from musician import Musician
    from guitar import Guitar

    band = Band()
    assert not band.name
    assert not band.musicians

    band.name = "Classical Classics"

    musician = Musician("Tom")
    musician.instruments.append(Guitar("Dick's Guitar", 1999, 1234.95))
    band.add(musician)

    non_musician = Musician("Harry")
    band.add(non_musician)

    print(band)
    print(band.play())
