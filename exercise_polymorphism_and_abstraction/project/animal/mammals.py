from project.animal.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    @property
    def food_that_eats(self):
        return [Fruit, Vegetable]

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    @property
    def food_that_eats(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    @property
    def food_that_eats(self):
        return [Meat, Vegetable]

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    @property
    def food_that_eats(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "ROAR!!!"
