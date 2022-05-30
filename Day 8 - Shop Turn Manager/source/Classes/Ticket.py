"""
Ticket object that contains section and num
"""
from Classes.TicketDecorator import decorate_ticket
from Classes.TurnGenerator import TurnGenerator
from Enums.Sections import Section


class Ticket:
    def __init__(self, section: Section, turn):
        self.section = section
        self.turn = turn
        self.id = section.value["name"][0:2] + str(self.turn)

    def __str__(self):
        return decorate_ticket(self)

