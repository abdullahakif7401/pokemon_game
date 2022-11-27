import unittest
from tester_base import TesterBase

from unittest import TestCase
from unittest.mock import patch
from pokemon import Charmander, Bulbasaur, Squirtle


class TestPokemon(TestCase):

    def test_charmander_string(self):
        charmander = Charmander()
        self.assertEqual("Charmander's HP = 7 and level = 1", charmander.__str__(), "string not correct for Charmander")

    def test_charmander_poketype(self):
        charmander = Charmander()
        self.assertEqual('FIRE', charmander.get_poke_type(), "poketype not correct for Charmander")

    def test_charmander_attributes(self):
        charmander = Charmander()
        self.assertEqual(4, charmander.get_defence(), "The defence should be 4")
        self.assertEqual(8, charmander.get_speed(), "The speed should be 7+1=8")
        self.assertEqual(7, charmander.get_attack(), "The attack damage should be 6+1=7")

    def test_bulbasaur_string(self):
        bulbasaur = Bulbasaur()
        self.assertEqual("Bulbasaur's HP = 9 and level = 1", bulbasaur.__str__(), "string not correct for Bulbasaur")

    def test_bulbasaur_poketype(self):
        bulbasaur = Bulbasaur()
        self.assertEqual('GRASS', bulbasaur.get_poke_type(), "poketype not correct for Bulbasaur")

    def test_bulbasaur_attributes(self):
        bulbasaur = Bulbasaur()
        self.assertEqual(5, bulbasaur.get_defence(), "The defence should be 4")
        self.assertEqual(7, bulbasaur.get_speed(), "The speed should be 7")
        self.assertEqual(5, bulbasaur.get_attack(), "The attack damage should be 5")

    def test_squirtle_string(self):
        squirtle = Squirtle()
        self.assertEqual("Squirtle's HP = 8 and level = 1", squirtle.__str__(), "string not correct for Squirtle")

    def test_squirtle_poketype(self):
        squirtle = Squirtle()
        self.assertEqual('WATER', squirtle.get_poke_type(), "poketype not correct for Squirtle")

    def test_squirtle_attributes(self):
        squirtle = Squirtle()
        self.assertEqual(7, squirtle.get_defence(), "The defence should be 7")
        self.assertEqual(7, squirtle.get_speed(), "The speed should be 7")
        self.assertEqual(4, squirtle.get_attack(), "The attack damage should be 4")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemon)
    unittest.TextTestRunner(verbosity=0).run(suite)