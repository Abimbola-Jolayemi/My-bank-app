from unittest import TestCase

import account

class TestAccount(TestCase):
    def setUp(self):
        self.account1 = account.Account("Abimbola Jolayemi", "0000", "1000000")
        self.account2 = account.Account("Jonah Odoh", "2222", "1010101")

    def test_that_account_exists(self):
        account.Account("Abimbola Jolayemi", "0000", "1000000")

    def test_that_account_balance_is_zero(self):
        self.assertEqual(self.account1.balance, 0)

    def test_that_account_can_check_balance(self):
        self.assertEqual(self.account1.get_balance(), 0)

    def test_that_account_can_deposit(self):
        self.account1.deposit(2000)
        self.assertEqual(self.account1.balance, 2000)

    def test_that_account_cannot_deposit_negative_amount(self):
        self.account1.deposit(5000)
        with self.assertRaises(ValueError):
            self.account1.deposit(-2000)

    def test_that_account_cannot_deposit_zero_amount(self):
        self.account1.deposit(5000)
        with self.assertRaises(ValueError):
            self.account1.deposit(0)

    def test_that_account_can_withdraw(self):
        self.account1.deposit(5000)
        self.assertEqual(self.account1.balance, 5000)
        self.account1.withdraw(2000, "0000")
        self.assertEqual(self.account1.balance, 3000)

    def test_that_account_cannot_withdraw_with_incorrect_pin(self):
        self.account1.deposit(5000)
        with self.assertRaises(ValueError):
            self.account1.withdraw(2000, "1111")

    def test_that_account_cannot_withdraw_negative_amount(self):
        self.account1.deposit(5000)
        with self.assertRaises(ValueError):
            self.account1.withdraw(-2000, "0000")

    def test_that_account_cannot_withdraw_zero_amount(self):
        self.account1.deposit(5000)
        with self.assertRaises(ValueError):
            self.account1.withdraw(0, "0000")

    def test_that_account_cannot_withdraw_above_account_balance(self):
        self.account1.deposit(5000)
        with self.assertRaises(ValueError):
            self.account1.withdraw(7000, "0000")

    def test_that_account_can_update_pin(self):
        self.account1.deposit(5000)
        self.account1.update_pin("0000", "1111")
        self.account1.withdraw(2000, "1111")
        self.assertEqual(self.account1.balance, 3000)

    def test_change_pin_new_pin_is_not_equal_to_old_pin(self):
        self.account1.deposit(5000)
        with self.assertRaises(ValueError):
            self.account1.update_pin("0000", "0000")

    def test_that_pin_length_is_four(self):
        with self.assertRaises(ValueError):
            self.account1.update_pin("0000", "12345")

    def test_that_pin_contains_numbers_alone(self):
        self.account1.deposit(5000)
        with self.assertRaises(ValueError):
            self.account1.withdraw(2000, "aaaa")