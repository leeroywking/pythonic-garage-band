from pythonic_garage_band.Musician import Musician


class Guitarist(Musician):
    def __init__(self, name: str):
        self.instrument = "Guitar"
        self.name = name
        pass
