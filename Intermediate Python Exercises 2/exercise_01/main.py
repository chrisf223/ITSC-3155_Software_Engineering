import BankAccount

bank = BankAccount.BankAccount("Chris",800.0)
bank.deposit_money(450.0)
bank.withdraw_money(47)
print(bank.get_balance())