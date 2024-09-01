from account import Account

class Bank:

    def __init__(self):
        self.accounts = []
        self.next_account_number = 10000000
        self.account_number = str(self.next_account_number)
        self.number_of_accounts = 0

    def create_account(self, first_name, last_name, pin, account_number) -> Account:
        if len(pin) != 4 or not pin.isdigit():
            raise ValueError("PIN must be exactly 4 digits.")
        name = first_name + ' ' + last_name
        self.next_account_number += 1
        self.account_number = str(self.next_account_number)
        new_account = Account(name, pin, account_number)
        self.accounts.append(new_account)
        self.number_of_accounts += 1
        return new_account

    def get_number_of_accounts(self):
        return self.number_of_accounts

    def validate_account_number(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def deposit(self, amount, account_number):
        found_account_number = self.validate_account_number(account_number)
        if found_account_number is not None:
            found_account_number.deposit(amount)
            return "Account deposit successful"
        else:
            return "Account not found"

    def withdraw(self, amount, account_number ,pin):
        found_account_number = self.validate_account_number(account_number)
        if found_account_number is not None:
            if found_account_number.validate_pin(pin):
                found_account_number.withdraw(amount, pin)
                return "Account withdraw successful"
            else:
                return "Invalid pin"
        else:
            return "Account not found"

    def transfer(self, sender_account_number, recipient_account_number, amount, senders_pin):
        if sender_account_number is not recipient_account_number:
            self.withdraw(amount, sender_account_number, senders_pin)
            self.deposit(amount, recipient_account_number)
            return "Transfer successful"
        else:
            return "Invalid recipient's account number"

    def delete_account(self, account_number):
        account_to_delete = self.validate_account_number(account_number)
        if account_to_delete:
            self.accounts.remove(account_to_delete)
            self.number_of_accounts -= 1
            return "Account deleted successfully"
        else:
            return "Account not found"

    def display_option(self):
        print("""
            1. Create account
            2. Deposit
            3. Withdraw
            4. Transfer
            5. Close account
            """)