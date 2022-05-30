"""
Ticket object that contains section and num
"""
from Enums.Sections import Section

class Ticket:
    def __init__(self, section: Section, num):
        self.section = section
        self.num = num
        self.id = section.value[0:2] + str(num)
