from bank import Bank


def main():
    bank = Bank()

    print("********************************")
    print("Welcome to Bank App")
    print()

    while True:
        bank.display_option()
        option = input("Enter your choice: ")
        print("********************************")

        if option in ["1", "2", "3", "4", "5"]:
            match option:
                case "1":
                    first_name = input("Enter your first name: ")
                    last_name = input("Enter your last name: ")

                    while True:
                        pin = input("Enter your 4-digit pin: ")
                        if len(pin) != 4 or not pin.isdigit():
                            print("Error: PIN must be exactly 4 digits.")
                        else:
                            account_number = bank.account_number
                            new_account = bank.create_account(first_name, last_name, pin, account_number)
                            print("Your account has been created")
                            print(f"""DETAILS: 
                                Name: {new_account.name} 
                                PIN: ****
                                Account Number: {new_account.account_number} 
                                """)
                            break

                case "2":
                    account_number = input("Enter your account number: ")
                    found_account = bank.validate_account_number(account_number)
                    if found_account is None:
                        print("Error: Account number not found!!!")
                        print("Please try again.")
                    else:
                        amount = int(input("Enter amount to be deposited: "))
                        bank.deposit(amount, account_number)
                        print(f"#{amount} has been deposited into account: {account_number}")

                case "4":
                    while True:
                        sender_account_number = input("Enter sender account number: ")
                        found_sender_account = bank.validate_account_number(sender_account_number)
                        if found_sender_account is not None:
                            break
                        print("Error: Sender account number not found. Please try again.")

                    while True:
                        receiver_account_number = input("Enter receiver account number: ")
                        found_receiver_account = bank.validate_account_number(receiver_account_number)
                        if found_receiver_account is not None and receiver_account_number != sender_account_number:
                            break
                        print("Error: Receiver account number not found. Please try again.")

                    while True:
                        amount = input("Enter amount to be transferred: ")
                        if amount.isdigit() and int(amount) > 0:
                            amount = int(amount)
                            break
                        print("Error: Invalid amount. Please enter a positive number.")

                    while True:
                        pin = input("Enter sender's PIN: ")
                        if found_sender_account.validate_pin(pin):
                            break
                        print("Error: Invalid PIN. Please try again.")

                    bank.withdraw(amount, sender_account_number, pin)
                    bank.deposit(amount, receiver_account_number)
                    print(
                        f"#{amount} has been transferred from account {sender_account_number} to {receiver_account_number}")




if __name__ == "__main__":
    main()