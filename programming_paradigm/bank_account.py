#bank_account.py

class BankAccount:
    def __init__(self, initial_account_balance=0):
        self.account_balance = initial_account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

import sys

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

#Examples
# Examples (run in terminal):
# python bank_account.py deposit:50
# python bank_account.py display
# python bank_account.py withdraw:20
# python bank_account.py display
# python bank_account.py withdraw:150
# python bank_account.py display
