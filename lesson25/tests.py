import unittest

from main import BankAccount, InsufficientFunds

class TestNewAccount(unittest.TestCase):
    def test_creation(self):
        new_account = BankAccount()
        self.assertEqual(new_account.get_balance(), 0)

    def test_if_balance_custom(self):
        new_account = BankAccount(100)
        self.assertEqual(new_account.get_balance(), 100)

class TestAccountDeposit(unittest.TestCase):
    def test_deposit_increase_balance(self):
        account = BankAccount()
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)

    def test_deposit_zero_raises_value_error(self):
        account = BankAccount()
        with self.assertRaises(ValueError):
            account.deposit(0)

    def test_deposit_negative_raises_value_error(self):
        account = BankAccount()
        with self.assertRaises(ValueError):
            account.deposit(-100)

    def test_deposit_invalid_type_raises_error(self):
        account = BankAccount()
        with self.assertRaises(TypeError):
            account.deposit("100")

class TestAccountWithdrawal(unittest.TestCase):
    def test_withdraw_decrease_balance(self):
        account = BankAccount(200)
        account.withdraw(20)
        self.assertEqual(account.get_balance(), 180)

    def test_withdraw_zero_raises_value_error(self):
        account = BankAccount(200)
        with self.assertRaises(ValueError):
            account.withdraw(0)

    def test_withdraw_negative_raises_value_error(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.withdraw(-90)

    def test_withdraw_more_than_balance(self):
        accout = BankAccount(100)
        with self.assertRaises(InsufficientFunds):
            accout.withdraw(110)

    def test_withdraw_invalid_type_raises_error(self):
        account = BankAccount()
        with self.assertRaises(TypeError):
            account.withdraw("100")

class TestAccountTransfers(unittest.TestCase):
    def test_transfer_to_not_account(self):
        account = BankAccount(100)
        with self.assertRaises(TypeError):
            account.transfer("not_account", 50)

    def test_transfer_movement(self):
        account_1 = BankAccount(100)
        account_2 = BankAccount(200)
        account_1.transfer(account_2, 70)
        self.assertEqual(account_1.get_balance(),30)
        self.assertEqual(account_2.get_balance(), 270)

    def test_negative_transfer_sum(self):
        account_1 = BankAccount(100)
        account_2 = BankAccount(200)
        with self.assertRaises(ValueError):
            account_1.transfer(account_2, -70)

    def test_not_enough_funds_to_transfer(self):
        account_1 = BankAccount(100)
        account_2 = BankAccount(200)
        with self.assertRaises(InsufficientFunds):
            account_1.transfer(account_2, 150)

class TestBalanceCheck(unittest.TestCase):
    def test_get_balance_positive_scenario(self):
        account = BankAccount(1745)
        self.assertEqual(account.get_balance(), 1745)

    def test_get_balance_after_operations(self):
        account = BankAccount()
        account.deposit(1000)
        account.withdraw(320)
        account.deposit(20)
        account.withdraw(1)
        self.assertEqual(account.get_balance(), 699)

if __name__ == '__main__':
    unittest.main()



