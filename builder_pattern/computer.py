class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None  # in gigabytes
        self.hdd = None  # in gigabytes
        self.gpu = None

    def __str__(self):
        info = (
            "Memory: {}GB".format(self.memory),
            "Hard Disk: {}GB".format(self.hdd),
            "Graphics Card: {}".format(self.gpu),
        )
        return "\n".join(info)


def test_computer():
    computer = Computer("123456")
    assert type(str(computer)) is str
