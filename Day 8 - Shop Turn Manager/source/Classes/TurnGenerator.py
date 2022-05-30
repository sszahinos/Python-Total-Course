"""
Class with a ticket generator.
"""
from Enums.Sections import Section

class TurnGenerator:

    def __init__(self, section: Section):
        self.section = section.value["name"]
        self.max_turns = section.value["max_turns"]
        self.current_turn = 0

    def get_turn(self):
        for num in range(1, self.max_turns + 1):
            self.current_turn += 1
            yield num

