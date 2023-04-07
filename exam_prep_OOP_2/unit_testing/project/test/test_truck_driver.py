from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.truck_driver = TruckDriver("Will", 10.1)

    def test_init(self):
        self.assertEqual("Will", self.truck_driver.name)
        self.assertEqual(10.1, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_setter_earned_money(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -1

        self.assertEqual("Will went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_exception(self):
        pass

if __name__ == "__main__":
    main()