"""
Class with a ticket generator.
"""

class TurnGenerator:

    def __init__(self, section: str, max_turns: int):
        self.section = section
        self.max_turns = max_turns

    def get_turn(self):
        try:
            for num in range(1, self.max_turns + 1):
                yield num
        except StopIteration:
            print("No more turn tickets left.")
            return -1

    def get_section(self):
        return self.section
