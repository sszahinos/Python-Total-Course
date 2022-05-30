import unittest
from Classes.Ticket import Ticket
from Enums.Sections import Section


class TestTicket(unittest.TestCase):
    def test_id(self):
        ticket = Ticket(Section.PHARMACY, 1)
        test_value = ticket.id
        desired_value = "PH1"
        self.assertEqual(test_value, desired_value, "test_id")



