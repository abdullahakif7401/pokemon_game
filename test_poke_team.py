import unittest

from tester_base import TesterBase, captured_output
from poke_team import PokeTeam

class TestPokeTeam(TesterBase):

    def test_choose_team(self):
        from poke_team import PokeTeam
        try:
            team = PokeTeam("Brock")
        except Exception as e:
            self.verificationErrors.append(f"Brock's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("4 4 1\n1 2 1\n2 2 2") as (inp, out, err):
                # 4 4 1 should fail, since it is too many pokemon. Also 1 2 10
                # So 2 2 2 should be the correct team.
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Brock's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()

        # Check the prompt is being printed.
        try:
            assert "is the number of Charmanders" in output
            assert "is the number of Bulbasaurs" in output
            assert "is the number of Squirtles" in output
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not print prompt correctly.")
        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    def test_assign_team(self):
        from poke_team import PokeTeam
        try:
            team = PokeTeam("Brock")
        except Exception as e:
            self.verificationErrors.append(f"Brock's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1") as (inp, out, err):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Brock's team could not be chosen: {str(e)}.")
            return
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokeTeam)
    unittest.TextTestRunner(verbosity=0).run(suite)
