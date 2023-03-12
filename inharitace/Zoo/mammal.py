from PlayersAndMonsters import Animal


class Mammal(Animal):
    def __init__(self, name: str):
        Animal.__init__(self, name)