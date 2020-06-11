from pythonic_garage_band.Musician import Musician


class Vocalist(Musician):
    def __init__(self, name: str):
        self.instrument = "Vocals"
        self.name = name
        pass

    def __repr__(self):
        return f"Vocalist repr"

    def __str__(self):
        return f"Vocalist str"

   