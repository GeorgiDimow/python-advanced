from reptile import Reptile


class Snake(Reptile):
    def __init__(self, name: str):
        Reptile.__init__(self, name)