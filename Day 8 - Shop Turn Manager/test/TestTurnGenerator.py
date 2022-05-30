import unittest
from Enums.Sections import Section
from Classes.TurnGenerator import TurnGenerator


class TestTurnGenerator(unittest.TestCase):
    def test_get_turn(self):
        tg = TurnGenerator(Section.PHARMACY).get_turn()
        test_value = next(tg)
        desired_value = 1
        self.assertEqual(desired_value, test_value)
        test_value = next(tg)
        desired_value = 2
        print(test_value)
        self.assertEqual(desired_value, test_value)

