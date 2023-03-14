from project.animal.animal import Bird
from project.food import *


class Owl(Bird):
    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def food_that_eats(self):
        return [Meat, Food, Fruit, Vegetable, Seed]

    @property
    def gained_weight(self):
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"