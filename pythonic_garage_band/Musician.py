class Musician:
    def __init__(self, name: str):
        self.name = name
        self.instrument = ""
        pass

    def __repr__(self):
        return f"name:{self.name} instrument:{self.instrument}"

    def __str__(self):
        return f"{self.name}"
        

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return f"{self.name} plays a sick solo with their {self.instrument}"