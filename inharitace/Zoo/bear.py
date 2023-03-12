from mammal import Mammal


class Bear(Mammal):
    def __init__(self, name: str):
        Mammal.__init__(self, name)