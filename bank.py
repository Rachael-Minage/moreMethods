# Add these methods to class Account - deposit, withdraw. 
# Create two instances of account and verify they work as expected.
class Account:
    def __init__(self,account_number,account_name):
        self.balance = 0
        self.account_name = account_name
        self.account_number = account_number
        self.withdrawals = []
        self.deposits = []

    
    def deposit_check (self,amount):
        if amount<=0:
            return f"You cannot deposit {amount}."
        else:
            self.balance+=amount
            self.deposits.append(amount)
            return f"You have deposited {amount}, your balance is {self.balance}", self.deposits

    def withdrawal(self,amount):
        if amount>self.balance:
            return f"Your balance is {self.balance}, you cannot withdraw {amount}"
        elif amount<=0:
            return f"You cannot withdraw {amount}"
        else:
            self.balance-=amount
            self.withdrawals.append(amount)
            return f"You have withdrawn {amount}, your balance is {self.balance}", self.withdrawals
# Add a new method called deposits_statement which prints each deposit in a new line
    def deposits_statements(self):
        print(*self.deposits, sep = "\n")  
#  Add a new method called withdrawals_statement which prints each withdrawal in a new line
    def withdrawals_statement(self):
     print(*self.withdrawals, sep = "\n" )
    