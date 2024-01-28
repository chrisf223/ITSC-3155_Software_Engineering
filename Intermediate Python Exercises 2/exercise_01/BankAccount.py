class BankAccount():

    def __init__(self,account_name,starting_balance):
        self.account_name = account_name
        self.account_balance = starting_balance 

    def deposit_money(self,amount):
        self.account_balance += amount
    
    def withdraw_money(self,amount):
        self.account_balance -= amount

    def get_balance(self):
        return self.account_name + " has a balance of " + str(self.account_balance)

