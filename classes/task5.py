# Here is a class for a bank account
class Account:

    # Here is a constructor that saves the owner and balance
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Here is a method to add money to the account
    def deposit(self, amount):
        self.balance += amount
        print("Deposit:", amount)
        print("New balance:", self.balance)

    # Here is a method to withdraw money from the account
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal:", amount)
            print("New balance:", self.balance)
        else:
            print("Insufficient funds")


# Here is an Account object
account1 = Account("Amina", 1000)

# Here is a deposit
account1.deposit(500)

# Here is a withdrawal
account1.withdraw(300)

# Here is an attempt to withdraw too much money
account1.withdraw(2000)