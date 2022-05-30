import unittest
from Classes.Ticket import Ticket
from Enums.Sections import Section
from Classes.TicketDecorator import decorate_ticket


class TestTicketDecorator(unittest.TestCase):
    def test_decorate_ticket(self):
        ticket = Ticket(Section.PHARMACY, 1)
        test_value = decorate_ticket(ticket)
        desired_value = f"""---------------------------------------
| Welcome to Nice Shops INC. 
| Your turn is:
|   
| \t\tPH1
|
| Go to pharmacy and wait your turn.
|
| Respect the 1.5m space between
| other clients and remember
| that smoking is forbidden.
|
| Thank you and have a nice day.
---------------------------------------"""
        self.assertEqual(test_value, desired_value)

