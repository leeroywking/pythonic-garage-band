from pythonic_garage_band.Musician import Musician
from pythonic_garage_band.Vocalist import Vocalist
from pythonic_garage_band.Guitarist import Guitarist
from pythonic_garage_band.Bassist import Bassist
from pythonic_garage_band.Drummer import Drummer


bands = []


class Band:
    """
    Band class which contains members and can play solos
    """

    def __init__(self, name: str, members: list):
        self.name = name
        self.members = members
        bands.append(self)

    def __repr__(self):
        memberslist = str([member.name for member in self.members])
        # print(memberslist)
        output = f"members:{memberslist} name:{self.name}"
        return output

    def __str__(self):
        list_of_members = ""
        for member in self.members:
            list_of_members += member.name + " "
        return f"This class instantiates a band with members: {list_of_members} and a name:{self.name}"

    def play_solos(self):
        output = ""
        for member in self.members:
            output += member.play_solo() + "\n"
        return output

    def add_member(self, new_member: Musician):
        self.members.append(new_member)

    def to_list(self):
        return bands

    def get_musician_class(self, instrument: str):
        if instrument == "Vocals":
            return Vocalist
        elif instrument == "Guitar":
            return Guitarist
        elif instrument == "Bass Guitar":
            return Bassist
        elif instrument == "Drumset":
            return Bassist
        else:
            raise Exception("Invalid instrument")

    def create_from_data(self, new_members: [list]):
        self.members = []
        for member in new_members:
            name = member[0]
            instrument = member[1]
            position = self.get_musician_class(instrument)
            bandmate = position(name)
            self.members.append(bandmate)

    def save_band(self):
        output = []
        for member in self.members:
            output.append([member.name, member.instrument])
        return output
