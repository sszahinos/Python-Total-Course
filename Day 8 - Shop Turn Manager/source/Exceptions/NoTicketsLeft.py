class NoTicketsLeft(Exception):
    def __init__(self, message="No tickets available"):
        super(NoTicketsLeft, self).__init__(message)

