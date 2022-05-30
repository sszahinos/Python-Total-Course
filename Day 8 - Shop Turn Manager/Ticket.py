"""
Ticket object that contains section and num
"""

class Ticket:
    def __init__(self, section, num):
        self.section = section
        self.num = num
        self.id = section[0:2] + str(num)
