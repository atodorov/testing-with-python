import pytest

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

@pytest.fixture
def account_for_alex():
    return BankAccount('Alex', 'Demo Account', 100, 'EUR')

@pytest.fixture
def bobs_account():
    return BankAccount('Bob', 'Retirement Account', 0, 'EUR')


def test_create_with_initial_deposit_should_set_ballance_correctly(account_for_alex):
    assert 100 == account_for_alex.balance
    assert 'EUR' == account_for_alex.currency


# with fixtures. setup is -------------------------vvv     and      vvv
def test_transfer_should_change_balance_for_both(account_for_alex, bobs_account):
    account_for_alex.transfer(30, bobs_account)
    assert 70 == account_for_alex.balance
    assert 30 == bobs_account.balance

# without fixtures
def test_create_with_initial_deposit_should_set_ballance_correctly():
    # vvv setup is this line
    account = BankAccount('Alex', 'Demo Account', 100, 'EUR')
    assert 100 == account.balance
