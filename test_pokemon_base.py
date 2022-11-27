import unittest
from tester_base import TesterBase

from unittest import TestCase
from unittest.mock import patch
from pokemon_base import PokemonBase

class TestPokemonBase(TestCase):
    @patch("pokemon_base.PokemonBase.__abstractmethods__", set())
    def test_get_set_hp(self):
        pokemonBase= PokemonBase(100, 'water')
        self.assertEqual(100, pokemonBase.get_hp(), "Hp returned is not correct should be 100")
        pokemonBase.set_hp(75)
        self.assertEqual(75, pokemonBase.get_hp(), "Hp returned is not correct should be 75 after set")

    @patch("pokemon_base.PokemonBase.__abstractmethods__", set())
    def test_get_poketype(self):
        pokemonBase= PokemonBase(10, 'water')
        self.assertEqual('water', pokemonBase.get_poke_type(), "type should be water")

    @patch("pokemon_base.PokemonBase.__abstractmethods__", set())
    def test_is_fainted(self):
        pokemonBase= PokemonBase(10, 'water')
        self.assertEqual(False, pokemonBase.is_fainted(), "Pokemon should not be fainted")

    @patch("pokemon_base.PokemonBase.__abstractmethods__", set())
    def test_get_level(self):
        pokemonBase= PokemonBase(10, 'water')
        self.assertEqual(1, pokemonBase.get_level(), "Level should be 1")

    @patch("pokemon_base.PokemonBase.__abstractmethods__", set())
    def test_level_up(self):
        pokemonBase= PokemonBase(10, 'water')
        pokemonBase.level_up()
        self.assertEqual(2, pokemonBase.get_level() , "Level should be 2")

    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemonBase)
    unittest.TextTestRunner(verbosity=0).run(suite)
