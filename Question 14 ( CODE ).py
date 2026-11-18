# Bank Account System Using Object-Oriented Programming

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Enter a valid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def display_balance(self):
        print("Account holder:", self.account_holder)
        print("Current balance:", round(self.balance, 2))


name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n--- Bank Account Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.display_balance()
    elif choice == "4":
        print("Thank you for using the bank system.")
        break
    else:
        print("Invalid choice.")

# output
# Enter account holder name: tejesh

# --- Bank Account Menu ---
# 1. Deposit
# 2. Withdraw
# 3. Check balance
# 4. Exit
# Enter choice: 2
# Enter withdrawal amount: 123
# Insufficient balance.

# --- Bank Account Menu ---
# 1. Deposit
# 2. Withdraw
# 3. Check balance
# 4. Exit
# Enter choice: 