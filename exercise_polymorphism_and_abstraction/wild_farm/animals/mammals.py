from wild_farm.animals.animal import Mammal
from wild_farm.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    @property
    def gained_weight(self):
        return 0.10

    @property
    def food_that_eats(self):
        return [Fruit, Vegetable]

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    @property
    def gained_weight(self):
        return 0.40

    @property
    def food_that_eats(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    @property
    def gained_weight(self):
        return 0.30

    @property
    def food_that_eats(self):
        return [Meat, Vegetable]

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    @property
    def gained_weight(self):
        return 1.00

    @property
    def food_that_eats(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "ROAR!!!"
