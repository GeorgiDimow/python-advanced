from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("Grigor", 35, 100)
        self.tennis_player_2 = TennisPlayer("Tanya", 25, 92.34)

    def test_correct__init(self):
        assert self.tennis_player.name == "Grigor"
        assert self.tennis_player.age == 35
        assert self.tennis_player.points == 100
        assert not self.tennis_player.wins
        assert isinstance(self.tennis_player.wins, list)

    def test_name_setter_value_len_under_2_sym(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player_2.name = ''

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_setter_value_under_18(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player_2.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_correct(self):
        self.tennis_player_2.add_new_win("Rolex Shanghai Masters")

        self.assertEqual("Rolex Shanghai Masters", self.tennis_player_2.wins[0])

    def test_add_new_win_in_existing_tournament(self):
        self.tennis_player_2.add_new_win("Wimbledon")
        result = self.tennis_player_2.add_new_win("Wimbledon")

        self.assertEqual("Wimbledon has been already added to the list of wins!", result)

    def test_str(self):
        self.tennis_player_2.add_new_win("Wimbledon")
        self.tennis_player_2.add_new_win("Rolex Shanghai Masters")

        self.assertEqual(
            "Tennis Player: Tanya\n"
            f"Age: 25\n"
            f"Points: 92.3\n"
            f"Tournaments won: Wimbledon, Rolex Shanghai Masters",
            str(self.tennis_player_2)
        )

    def test_more_than_operator(self):

        self.assertEqual(
            'Grigor is a better player than Tanya',
            self.tennis_player_2 > self.tennis_player
        )

    def test_less_than_operator(self):

        self.assertEqual(
            'Grigor is a top seeded player and he/she is better than Tanya',
            self.tennis_player > self.tennis_player_2
        )


if __name__ == "__main__":
    main()
