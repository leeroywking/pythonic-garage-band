from pythonic_garage_band import __version__
from pythonic_garage_band.Band import Band
from pythonic_garage_band.Musician import Musician
from pythonic_garage_band.Vocalist import Vocalist
from pythonic_garage_band.Bassist import Bassist
from pythonic_garage_band.Guitarist import Guitarist
from pythonic_garage_band.Drummer import Drummer


def test_version():
    assert __version__ == "0.1.0"


def test_band_1():
    band1 = Band("The Pixies", [])
    assert band1.name == "The Pixies"


def test_band2():
    band2 = Band("The Ya Ya Ya's", [])
    assert band2.members == []


def test_band3():
    band3 = Band("Run the Jewels", [])
    member1 = Vocalist("Killer Mike")
    band3.add_member(member1)
    assert band3.members[0] == member1


def test_band4():
    band4 = Band("Point North", [])
    assert isinstance(band4.__repr__(), str)


def test_band5():
    band5 = Band("HONNE", [])
    assert len(band5.to_list()) == 5


def test_band_fail1():
    band6 = Band("MGMT", [])
    members = band6.members
    assert len(members) != 1


def test_vocalist1():
    vocals1 = Vocalist("Geddy Lee")
    assert vocals1.play_solo() == "Geddy Lee plays a sick solo with their Vocals"


def test_rush():
    geddy_lee_bass = Bassist("Geddy Lee")
    geddy_lee_vocals = Vocalist("Geddy Lee")
    neil_peart_drums = Drummer("Neil Peart")
    rush = Band("Rush", [geddy_lee_bass, geddy_lee_vocals, neil_peart_drums])
    solos = rush.play_solos()
    expected = "Geddy Lee plays a sick solo with their Bass Guitar\nGeddy Lee plays a sick solo with their Vocals\nNeil Peart plays a sick solo with their Drumset\n"
    assert solos == expected


def test_garfunkle_and_oats_save():
    kate = Vocalist("Kate Micucci")
    riki = Vocalist("Riki Lindhome")
    gfao = Band("Garfunkle and Oats", [kate, riki])
    gfao_saved = gfao.save_band()
    assert gfao_saved == [["Kate Micucci", "Vocals"], ["Riki Lindhome", "Vocals"]]


def test_garfunkle_and_oats_load():
    kate = Vocalist("Kate Micucci")
    riki = Vocalist("Riki Lindhome")
    gfao = Band("Garfunkle and Oats", [kate, riki])
    gfao_saved = gfao.save_band()
    new_gfao = Band("Garfunkle and Oats2!", [])
    new_gfao.create_from_data(gfao_saved)
    new_gfao_solos = new_gfao.play_solos()
    assert (
        new_gfao_solos
        == "Kate Micucci plays a sick solo with their Vocals\nRiki Lindhome plays a sick solo with their Vocals\n"
    )


def test_band_str():
    band1 = Band("Smashing Pumpkins", [])
    band1.add_member(Vocalist("William Patrick CorganJr."))
    expectedout = "This class instantiates a band with members: William Patrick CorganJr.  and a name:Smashing Pumpkins"
    assert str(band1) == expectedout
