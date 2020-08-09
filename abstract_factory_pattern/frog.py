class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print(
            "{} the Frog encounters {} and {}!".format(
                self, obstacle, obstacle.action()
            )
        )


def test_frog():
    frog = Frog("allan")
    # print(frog)
    # assert type(str(frog)) is str
    assert str(frog) == "allan"
