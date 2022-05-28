import unittest
from random import randint

MAX_ACCOUNTS = 500


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
        return f"Name: {self.surname}, {self.name}\nAccount num.: {self.acc_num}\nBalance: {self.balance}"

    def diposit(self, ammount):
        self.balance += ammount
        return self.ammount

    def check_withdraw(self, ammount):
        return ammount >= self.balance

    def withdraw(self, ammount):
        if check_withdraw(ammount):
            self.balance -= ammount
        return self.ammount

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

    def __check_client(self, client: Client):
        return any(cl.acc_num == client.acc_num for cl in self.client_list)


def start():
    pass


def ask_name():
    return input("Your name: ")


def ask_surname():
    return input("Your surname: ")


def register_client():
    client = Client(ask_name(), ask_surname())


def show_menu():
    pass


def ask_option():
    pass


def check_withdraw():
    pass


def exit():
    print("Have a nice day.")


# start()


### Testing ###
# person client clients
class ClientTest(unittest.TestCase):
    name = "name"
    surname = "surname"
    acc_num = 1
    balance = 1
    client = Client(name, surname, acc_num, balance)

    def test_str(self):
        actual = str(self.client)
        expected = f"Name: {self.surname}, {self.name}\nAccount num.: {self.acc_num}\nBalance: {self.balance}"
        self.assertEqual(actual, expected)

    def test_diposit(self):
        actual = self.client.diposit(5)
        expected = 6
        self.assertEqual(actual, expected)

    def test_wihtdraw_ok(self):
        actual = self.client.withdraw(1)
        expected = 0
        self.assertEqual(actual, expected)

    def test_withdraw_notok(self):
        actual_balance = self.balance
        actual = self.client.withdraw(500)
        expected = actual_balance
        self.assertEqual(actual, expected)

    def test_register(self):
        actual = self.client.register(5)
        expected = 5


    def execute(self):
        for meth in self.__dir__():
            meth()

client_test = ClientTest()
client_test.execute()
