import unittest


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



class TestBankAccount(unittest.TestCase):
    def test_create_with_initial_deposit_should_set_ballance_correctly(self):
        account = BankAccount('Alex', 'Demo Account', 100, 'EUR')
        self.assertEqual(100, account.balance)

    def test_create_with_negative_initial_deposit_should_raise_exception(self):
        with self.assertRaises(RuntimeError):
            pass
            # fill-in the test case

    def test_deposit_should_increase_balance(self):
        pass
        # fill-in the test case

    def test_negative_deposit_should_raise_exception(self):
        pass
        # fill-in the test case

    def test_withdraw_should_decrease_balance(self):
        pass
        # fill-in the test case

    def test_negative_withdraw_should_raise_exception(self):
        pass
        # fill-in the test case

    def test_transfer_should_change_balance_for_both(self):
        pass
        # fill-in the test case

    def test_negative_transfer_should_raise_exception_and_not_change_balance_for_both(self):
        pass
        # fill-in the test case

if __name__ == "__main__":
    unittest.main()
