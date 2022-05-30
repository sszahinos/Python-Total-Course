"""
Ticket object that contains section and num
"""

class Ticket:
    def __init__(self, section, num):
        self.section = section
        self.num = num

    def get_section(self):
        return self.section

    def get_num(self):
        return self.num
