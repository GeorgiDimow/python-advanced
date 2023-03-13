from project.animal.animal import Bird
from project.food import *


class Owl(Bird):
    @property
    def food_that_eats(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def food_that_eats(self):
        return [Meat, Food, Fruit, Vegetable, Seed]

    @staticmethod
    def make_sound():
        return "Cluck"