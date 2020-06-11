from pythonic_garage_band.Musician import Musician


class Drummer(Musician):
    def __init__(self, name: str):
        self.instrument = "Drumset"
        self.name = name
        pass

    def __repr__(self):
        return f"Drummer repr"

    def __str__(self):
        return f"Drummer str"
