from unittest import TestCase
from bank import Bank
import account

class MyTestCase(TestCase):
    def setUp(self):
        self.bank = Bank()
        self.bank_account_1 = self.bank.create_account("Abimbola", "Jolayemi", "0000", "1000001")
        self.bank_account_2 = self.bank.create_account("Comfort", "Adegbite", "1111", "1000002")

    def test_that_bank_exist(self):
        self.assertIsInstance(self.bank, Bank)

    def test_that_bank_can_create_account(self):
        self.assertIsInstance(self.bank_account_1, account.Account)

    def test_that_numbers_of_accounts_is_4_when_four_accounts_are_created(self):
        self.bank_account_3 = self.bank.create_account("Funmilola", "Sanni", "0000", "1000003")
        self.bank_account_4 = self.bank.create_account("Johnson", "Oluwatosin", "1111", "1000004")
        self.assertEqual(self.bank.get_number_of_accounts(), 4)

    def test_that_bank_can_validate_account(self):
        validated_account = self.bank.validate_account_number("1000001")
        self.assertEqual(self.bank_account_1, validated_account)

    def test_that_bank_can_deposit_into_a_valid_account(self):
        self.bank.deposit(5000, "1000001")
        self.assertEqual(self.bank_account_1.get_balance(), 5000)

    def test_that_bank_can_withdraw_from_valid_account(self):
        self.bank.deposit(5000, "1000001")
        self.bank.withdraw(2000, "1000001", "0000")
        self.assertEqual(self.bank_account_1.get_balance(), 3000)

    def test_that_bank_can_transfer_from_user1_to_user2(self):
        self.bank.deposit(10000, "1000001")
        self.bank.transfer("1000001", "1000002", 5000, "0000")
        self.assertEqual(self.bank_account_1.get_balance(), 5000)
        self.assertEqual(self.bank_account_2.get_balance(), 5000)

    def test_that_bank_can_delete_an_account(self):
        result = self.bank.delete_account("1000001")
        self.assertEqual(result, "Account deleted successfully")

    def test_that_number_of_account_is_minus_one_when_bank_deletes_one_account(self):
        result = self.bank.delete_account("1000001")
        self.assertEqual(self.bank.get_number_of_accounts(), 1)

    def test_that_bank_can_not_delete_an_unexisting_account(self):
        result = self.bank.delete_account("1000004")
        self.assertEqual(result, "Account not found")
        self.assertEqual(self.bank.get_number_of_accounts(), 2)
