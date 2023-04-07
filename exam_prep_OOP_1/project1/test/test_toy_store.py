from unittest import TestCase, main

from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.toy_store = ToyStore()

        self.toy_store.add_toy("A", "Toy")

    def test_init(self):
        self.assertEqual({
            "A": "Toy",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)

    def test_add_toy_to_non_existing_shelf(self):

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("Y", "Toy")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_to_shelf_taken_by_the_same_toy(self):

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Toy")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_to_taken_shelf(self):

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Toy1")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_correct(self):
        result = self.toy_store.add_toy("B", "Toy")

        self.assertEqual(self.toy_store.toy_shelf["B"], "Toy")
        self.assertEqual("Toy:Toy placed successfully!", result)

    def test_remove_toy_to_non_existing_shelf(self):

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("Y", "Toy")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_to_nom_existing_toy(self):

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Toy1")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_correct(self):

        result = self.toy_store.remove_toy("A", "Toy")

        self.assertEqual(self.toy_store.toy_shelf["A"], None)
        self.assertEqual("Remove toy:Toy successfully!", result)


if __name__ == '__main__':
    main()