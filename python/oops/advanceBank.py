class BankAccount:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def display(self):
        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Account No:", self.acc_no)
        print("Balance:", self.balance)


# Savings Account (Inheritance)
class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(f"Interest added: ₹{interest}")


# Current Account (Inheritance)
class CurrentAccount(BankAccount):
    def __init__(self, name, acc_no, balance):
        super().__init__(name, acc_no, balance)
        self.overdraft_limit = 5000

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"₹{amount} withdrawn (Overdraft allowed).")
        else:
            print("Overdraft limit exceeded!")


# Main Program
accounts = []

while True:
    print("\n===== BANK MENU =====")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Display Accounts")
    print("6. Add Interest (Savings Only)")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        acc_no = input("Enter account number: ")
        balance = float(input("Enter balance: "))
        acc = SavingsAccount(name, acc_no, balance)
        accounts.append(acc)

    elif choice == 2:
        name = input("Enter name: ")
        acc_no = input("Enter account number: ")
        balance = float(input("Enter balance: "))
        acc = CurrentAccount(name, acc_no, balance)
        accounts.append(acc)

    elif choice == 3:
        acc_no = input("Enter account number: ")
        amount = float(input("Enter amount: "))
        for acc in accounts:
            if acc.acc_no == acc_no:
                acc.deposit(amount)

    elif choice == 4:
        acc_no = input("Enter account number: ")
        amount = float(input("Enter amount: "))
        for acc in accounts:
            if acc.acc_no == acc_no:
                acc.withdraw(amount)

    elif choice == 5:
        for acc in accounts:
            acc.display()

    elif choice == 6:
        for acc in accounts:
            if isinstance(acc, SavingsAccount):
                acc.add_interest()

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")