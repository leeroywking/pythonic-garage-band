from pythonic_garage_band.Musician import Musician


class Vocalist(Musician):
    def __init__(self, name: str):
        self.instrument = "Vocals"
        self.name = name
        pass
