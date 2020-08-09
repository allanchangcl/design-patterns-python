from builder_pattern import computer


# builder
class ComputerBuilder:
    def __init__(self):
        self.computer = computer.Computer("AG23385193")

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


def test_computer_builder():
    builder = ComputerBuilder()
    # assert type(builder) is object
    assert isinstance(builder, ComputerBuilder)
