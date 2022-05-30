from Classes import Ticket


def decorate_ticket(ticket: Ticket):
    return f"""---------------------------------------
| Welcome to Nice Shops INC. 
| Your turn is:
|   
| \t\t{ticket.id}
|
| Go to {str(ticket.section.value['name']).lower()} and wait your turn.
|
| Respect the 1.5m space between
| other clients and remember
| that smoking is forbidden.
|
| Thank you and have a nice day.
---------------------------------------"""