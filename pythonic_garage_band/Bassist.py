from pythonic_garage_band.Musician import Musician


class Bassist(Musician):
    def __init__(self, name: str):
        self.instrument = "Bass Guitar"
        self.name = name
        pass

    def __repr__(self):
        return f"Bassist repr"

    def __str__(self):
        return f"Bassist str"
