from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    @abstractmethod
    def drive(self, distance: float):
        ...

    @abstractmethod
    def refuel(self, fuel: float):
        ...


class Car(Vehicle):
    AIR_CONDITIONING = 0.9

    def drive(self, distance: float):
        consumption = (self.fuel_consumption + Car.AIR_CONDITIONING) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    AIR_CONDITIONING = 1.6

    def drive(self, distance: float):
        consumption = (self.fuel_consumption + Truck.AIR_CONDITIONING) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * 0.95