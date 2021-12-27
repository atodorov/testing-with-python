"""
This is the "bank" module which provides API for banking services.

Use it like this

>>> b = BankAccount('Alex', 'Savings Account', 100, 'EUR')
>>> b
<bank.BankAccount object at 0x...>
"""

class BankAccount:

    holder = None
    name = None
    balance = 0
    currency = None

    def __init__(self, holder, name, initial, currency):
        if initial < 0:
            raise RuntimeError('Initial deposit cannot be negative')

        self.holder = holder
        self.name = name
        self.balance += initial
        self.currency = currency

    def deposit(self, how_much):
        if how_much < 0:
            raise RuntimeError('Cannot deposit negative amount')

        self.balance += how_much

    def withdraw(self, how_much):
        if how_much < 0:
            raise RuntimeError('Cannot withdraw negative amount')

        if how_much > self.balance:
            raise RuntimeError('Cannot withdraw more than you have')

        self.balance -= how_much

    def transfer(self, how_much, to):
        self.withdraw(how_much)
        to.deposit(how_much)
