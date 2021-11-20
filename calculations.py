
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def add_string(a: str, b: str):
    return int(a) + int(b)


class InsufficientFunds(Exception):
    pass


class BankAccount:

    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return "Account balance: {}".format(self.balance)

    def transfer_to(self, other_account, amount):
        self.withdraw(amount)
        other_account.deposit(amount)
        return self.balance

    def transfer_from(self, other_account, amount):
        self.deposit(amount)
        other_account.withdraw(amount)
        return self.balance

    def __add__(self, other_account):
        return self.balance + other_account.balance

    def interest(self, rate):
        return self.balance * rate
