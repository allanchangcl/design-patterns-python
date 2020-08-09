class Bug:
    def __str__(self):
        return "a bug"

    def action(self):
        return "eats it"


def test_bug():
    bug = Bug()
    # print(bug.action())
    assert bug.action() == "eats it"
