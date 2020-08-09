from abstract_factory_pattern import bug
from abstract_factory_pattern import frog


# abstract factory method
class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t------ Frog World -------"

    def make_character(self):
        return frog.Frog(self.player_name)

    def make_obstacle(self):
        return bug.Bug()


def test_frog_world():
    frog_world = FrogWorld("allan")
    message = frog_world.make_character()
    # print(message)
    # print(frog_world.make_character())
    # assert type(str(frog)) is str
    assert str(message) == "allan"
