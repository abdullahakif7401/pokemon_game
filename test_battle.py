import unittest

from tester_base import TesterBase, captured_output
from battle import Battle

class TestTask3(TesterBase):

    def test_set_mode_battle(self):
        from battle import Battle

        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1 0\n0 2 1 0") as (inp, out, err):
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Ash"
        except AssertionError:
            self.verificationErrors.append(f"Ash should win: {result}.")

    def test_set_mode_battle_2(self):
        from battle import Battle

        try:
            b = Battle("Ash", "AnotherAsh")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1 0\n1 1 1 0") as (inp, out, err):
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Draw"
        except AssertionError:
            self.verificationErrors.append(f"It should be draw: {result}.")

    def test_rotating_mode_battle(self):
        from battle import Battle

        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1 0\n3 2 0 0") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Ash"
        except AssertionError:
            self.verificationErrors.append(f"Ash should win: {result}.")

    def test_rotating_mode_battle_2(self):
        from battle import Battle

        try:
            b = Battle("Ash", "Brock")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1 0\n1 1 1 0") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Draw"
        except AssertionError:
            self.verificationErrors.append(f"It should be draw: {result}.")

    def test_optimised_mode_battle_1(self):
        from battle import Battle

        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1 1\n0 2 3 0") as (inp, out, err):
                result = b.optimised_mode_battle('hp', 'lvl')
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Ash"
        except AssertionError:
            self.verificationErrors.append(f"Ash should win: {result}.")

    def test_optimised_mode_battle_2(self):
        from battle import Battle

        try:
            b = Battle("Ash", "Brock")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1 1\n1 1 1 1") as (inp, out, err):
                result = b.optimised_mode_battle('hp', 'attack')
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Brock"
        except AssertionError:
            self.verificationErrors.append(f"It should be Ash: {result}.")




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask3)
    unittest.TextTestRunner(verbosity=0).run(suite)
