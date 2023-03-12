from NeedForSpeed.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8


r = RaceMotorcycle(30, 100)
print(r.fuel_consumption)