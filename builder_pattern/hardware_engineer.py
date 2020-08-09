from builder_pattern import computer_builder


# director
class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = computer_builder.ComputerBuilder()
        [
            step
            for step in (
                self.builder.configure_memory(memory),
                self.builder.configure_hdd(hdd),
                self.builder.configure_gpu(gpu),
            )
        ]

    @property
    def computer(self):
        return self.builder.computer


def test_hardware_engineer():
    engineer = HardwareEngineer()
    engineer.construct_computer("16", "240", "nvidia")
    computer = engineer.computer
    # print(computer)
    assert type(str(computer)) is str
