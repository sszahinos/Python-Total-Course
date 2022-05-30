from Ticket import Ticket
from Sections import Section


def decorate_ticket(ticket: Ticket):
    return f"""Welcome to Nice Shops INC. 
Your turn is:
    
\t\t{ticket.id}

Go to {ticket.section.value} and wait your turn.

Remember to respect the 1.5m space
between other clients and
that smoking is forbidden.

Thank you and have a nice day."""
