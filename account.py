class Account:

    def __init__(self, name, pin, account_number):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount, pin):
        if pin != self.pin:
            print("Incorrect Pin")
            raise ValueError("Incorrect PIN")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        self.balance -= amount

    def validate_pin(self, pin):
        return pin == self.pin

    def update_pin(self, old_pin, new_pin):
        if old_pin != self.pin or len(new_pin) != 4 or new_pin == self.pin:
            raise ValueError("Incorrect PIN")
        if not new_pin.isdigit():
            raise ValueError("PIN must contain only digits")
        self.pin = new_pin

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number





