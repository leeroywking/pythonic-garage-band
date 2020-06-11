from pythonic_garage_band.Musician import Musician


class Guitarist(Musician):
    def __init__(self, name: str):
        self.instrument = "Guitar"
        self.name = name
        pass

    def __repr__(self):
        return f"Guitarist repr"

    def __str__(self):
        return f"Guitarist str"
