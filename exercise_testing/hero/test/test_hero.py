from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Spiderman", 10, 120, 10)
        self.enemy_hero = Hero("Batman", 10, 120, 10)

    def test_correct_initialization(self):
        self.assertEqual("Spiderman", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(120, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_username_equality_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_health_below_zero_raise_exception(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest",
                         str(ex.exception))

    def test_battle_enemy_health_below_zero_raise_exception(self):
        self.enemy_hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest",
                         str(ex.exception))

    def test_battle_draw(self):
        self.hero.health -= 20
        self.enemy_hero.health -= 20
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy_hero.health)
        self.assertEqual("Draw", result)

    def test_battle_lose(self):
        self.hero.damage -= 5
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(11, self.enemy_hero.level)
        self.assertEqual(75, self.enemy_hero.health)
        self.assertEqual(15, self.enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test_battle_win(self):
        self.hero.damage += 10
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(11, self.hero.level)
        self.assertEqual(25, self.hero.health)
        self.assertEqual(25, self.hero.damage)
        self.assertEqual(-80, self.enemy_hero.health)
        self.assertEqual("You win", result)

    def test_str(self):
        self.assertEqual("Hero Spiderman: 10 lvl\n"
                         "Health: 120\n"
                         "Damage: 10\n", str(self.hero))


if __name__ == "__main__":
    main()
