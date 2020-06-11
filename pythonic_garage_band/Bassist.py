from pythonic_garage_band.Musician import Musician


class Bassist(Musician):
    def __init__(self, name: str):
        self.instrument = "Bass Guitar"
        self.name = name
        pass
