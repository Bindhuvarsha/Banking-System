class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount <0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            return True
        self.balance -= amount
        return False

    def get_details (self):
        return (self.account_number, self.account_name, self.balance)

    