# Create a file called "BankAccount.py" and create a BankAccount class. The BankAccount class should have a constructor that takes in an account_name and starting_balance and stores them both as instance fields. 
## Create a method to deposit some amount of money into the account and another method which withdraws money from the account. 
## Also create a get_balance method which returns a string (does not print out, just returns) that says "{account_name} has a balance of {balance}". 
## In a separate file (you can just call it "app.py" or "main.py"), import the BankAccount class, instantiate it with a hardcoded account_name and starting_balance, deposit any amount, withdraw any amount, and then print out the result of calling the get_balance method on that class instance.

import BankAccount

bank = BankAccount.BankAccount("Chris",800.0)
bank.deposit_money(450.0)
bank.withdraw_money(47)
print(bank.get_balance())