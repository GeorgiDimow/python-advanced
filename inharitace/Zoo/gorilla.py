from mammal import Mammal


class Gorilla(Mammal):
    def __init__(self, name: str):
        Mammal.__init__(self, name)