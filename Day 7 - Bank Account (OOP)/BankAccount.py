# Not all cases controlled.

from os import system
import unittest
from random import randint

MAX_ACCOUNTS = 500
MENU_ITEMS = ["Exit", "Register", "Diposit", "Withdraw", "Show account data"]  # delete?


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


class Client(Person):
    def __init__(self, name: str, surname: str, acc_num: int = -1, balance: float = 0):
        super().__init__(name, surname)
        self.acc_num = acc_num
        self.balance = balance

    def __str__(self):
        return f"Name: {self.surname}, {self.name} | Account num.: {self.acc_num} | Balance: {self.balance}"

    def diposit(self, ammount: float):
        self.balance += ammount
        return self.balance

    def check_withdraw(self, ammount: float):
        return self.balance - ammount >= 0

    def withdraw(self, ammount: float):
        withdraw_ok = False
        if self.check_withdraw(ammount):
            self.balance -= ammount
            withdraw_ok = True
        return self.balance, withdraw_ok

    def register(self, acc_num):
        self.acc_num = acc_num
        return self.acc_num

    def unregister(self):
        self.acc_num = -1
        return self.acc_num


class Clients:
    def __init__(self):
        self.client_list = []

    def add_client(self, client: Client):
        added = False
        if not self.__check_client(client):
            client.register(len(self.client_list) + 1)
            self.client_list.append(client)
            added = True
        return added, client

    def remove_client(self, client: Client):
        removed = False
        if self.__check_client(client):
            client.unregister()
            self.client_list.remove(client)
            removed = True
        return removed, client

    def get_client(self, acc_num: int) -> Client:
        return self.client_list[acc_num]

    def __check_client(self, client: Client):
        return any(cl.acc_num == client.acc_num for cl in self.client_list)


def start():
    clients = Clients()
    finish = False
    while not finish:
        show_menu()
        option = ask_option()
        if not check_option(option):
            clear()
            print("Wrong selection")
            continue
        if int(option) == 1:
            finish = True
            exit()
        elif int(option) == 2:
            register(clients)
        elif int(option) == 3:
            diposit(clients)
        elif int(option) == 4:
            withdraw(clients)
        elif int(option) == 5:
            show_clients(clients)
        option = ""


def show_menu():
    global MENU_ITEMS
    print("Select an option:")
    for index, item in enumerate(MENU_ITEMS):
        print(f"{index + 1}. {item}")


def ask_option():
    return input("Select an option --> ")


def check_option(option):
    correct = False
    if check_int(option) and int(option) in range(1, len(MENU_ITEMS) + 1):
        correct = True
    return correct


def clear():
    system("cls")


def exit():
    print("Have a nice day.")


def register(clients):
    name = ask_name()
    surname = ask_surname()
    if register_client(clients, Client(name, surname)):
        print("Client registered.")
    else:
        print("This client is already registered")


def ask_name():
    return input("Your name: ")


def ask_surname():
    return input("Your surname: ")


def register_client(clients, client):
    return clients.add_client(client)


def diposit(clients):
    diposit_ok = False
    acc_num = ask_client()
    if check_int(acc_num):
        client = clients.get_client(int(acc_num)-1)
        client.diposit(float(ask_ammount()))
        diposit_ok = True

    if diposit_ok:
        print("Saved correctly.")
    else:
        print("An error with your diposit has ocurred.")


def ask_client():
    return input("Your account ID --> ")


def ask_ammount():
    return input("Ammount --> ")


def check_int(text):
    return text.isnumeric()


def withdraw(clients):
    withdraw_ok = False
    acc_num = ask_client()
    if check_int(acc_num):
        client = clients.get_client(int(acc_num)-1)
        ammount, withdraw_ok = client.withdraw(float(ask_ammount()))

    if withdraw_ok:
        print("Saved correctly.")
    else:
        print("An error with your diposit has ocurred.")


def show_clients(clients):
    if len(clients.client_list) == 0:
        print("0 clients registered.")
    else:
        for client in clients.client_list:
            print(client)


start()
"""
### Testing ###
class ClientTest(unittest.TestCase):
    name = "name"
    surname = "surname"
    acc_num = 1
    balance = 1

    def test_str(self):
        client = Client(self.name, self.surname, self.acc_num, self.balance)
        actual = str(client)
        expected = f"Name: {self.surname}, {self.name}\nAccount num.: {self.acc_num}\nBalance: {self.balance}"
        self.assertEqual(actual, expected)

    def test_diposit(self):
        client = Client(self.name, self.surname, self.acc_num, self.balance)
        actual = client.diposit(5)
        expected = 6
        self.assertEqual(actual, expected)

    def test_wihtdraw_ok(self):
        client = Client(self.name, self.surname, self.acc_num, self.balance)
        actual = client.withdraw(1)
        expected = 0
        self.assertEqual(actual, expected)

    def test_withdraw_notok(self):
        client = Client(self.name, self.surname, self.acc_num, self.balance)
        actual_balance = self.balance
        actual = client.withdraw(500)
        expected = actual
        self.assertEqual(actual, expected)

    def test_register(self):
        pass

    def execute(self):
        self.test_str()
        self.test_diposit()
        self.test_wihtdraw_ok()
        self.test_withdraw_notok()
        self.test_register()


class ClientsTest(unittest.TestCase):
    def test_add_client_ok(self):
        clients = Clients()
        clients.add_client(Client("name1", "surname1", 1, 0))
        clients.add_client(Client("name2", "surname2"))
        self.assert_()

    def test_add_client_not_ok(self):
        pass

    def test_remove_client_ok(self):
        pass

    def test_remove_client_not_ok(self):
        pass

    def execute(self):
        pass


client_test = ClientTest()
clients_test = ClientsTest()

client_test.execute()
clients_test.execute()
"""
