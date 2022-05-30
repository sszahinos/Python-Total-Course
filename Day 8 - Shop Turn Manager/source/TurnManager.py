from Classes.Ticket import Ticket
from Classes.TurnGenerator import TurnGenerator
from Enums.Sections import Section
from Exceptions.NoTicketsLeft import NoTicketsLeft
from os import system

def start():
    finish = False
    sections = [sec for sec in Section]
    generators = []
    for sec in sections:
        turn_generator = TurnGenerator(sec)
        generators.append([turn_generator, turn_generator.get_turn()])

    while not finish:
        print("Welcome to Nice Shops INC!")
        show_sections(sections)

        option = int(ask_section(sections)) - 1
        selected_section = sections[option]
        try:
            if generators[option][0].current_turn == sections[option].value["max_turns"]:
                raise NoTicketsLeft
            turn = next(generators[option][1])
        except NoTicketsLeft as e:
            print(e)
        else:
            ticket = Ticket(selected_section, turn)
            clear()
            print(ticket)

        option = input("Press enter to continue or E to exit... ")
        if not option.isnumeric() and str(option).upper() == "E":
            finish = True
        clear()
    print("Have a nice day")

def clear():
    system("cls")

def show_sections(sections):
    for index, sec in enumerate(sections):
        print(f"{index + 1}. {str(sec.value['name']).title()}")


def ask_section(sections) -> int:  # Assuming the screen will show only the correct options
    return input("Select the section to go --> ")

if __name__ == '__main__':
    start()
