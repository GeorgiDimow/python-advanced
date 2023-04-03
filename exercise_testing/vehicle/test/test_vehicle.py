from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(80.3, 500.6)

    def test_default_fuel_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_initializing(self):
        self.assertEqual(80.3, self.vehicle.fuel)
        self.assertEqual(500.6, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_without_fuel_raises_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_expect_fuel_decrease(self):
        self.vehicle.drive(2)
        self.assertEqual(77.8, self.vehicle.fuel)

    def test_refuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_increase_fuel(self):
        self.vehicle.fuel = 40.2
        self.vehicle.refuel(20)
        self.assertEqual(60.2, self.vehicle.fuel)

    def test_str(self):
        self.assertEqual("The vehicle has 500.6 horse power "
                         "with 80.3 fuel left and 1.25 fuel consumption", str(self.vehicle))


if __name__ == "__main__":
    main()
