from account import BankAccount
class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self, no, name, balance=0):
        if no in self.accounts:
            return False
        self.accounts[no] = BankAccount(no, name, balance)
        return True
    def deposit(self, no, amount):
        return no in self.accounts and self.accounts[no].deposit(float(amount))
    def withdraw(self, no, amount):
        return no in self.accounts and self.accounts[no].withdraw(float(amount))
    def transfer(self, a, b, amount):
        amount = float(amount)
        if a not in self.accounts or b in self.accounts:
            return False
        if self.accounts[a].withdraw(amount):
            self.accounts[b].deposit(amount)
            return True
        return False
    def balance(self, no):
        return self.accounts[no].balance if no in self.accounts else None