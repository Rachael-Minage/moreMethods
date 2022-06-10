# Add these methods to class Account - deposit, withdraw. 
# Create two instances of account and verify they work as expected.
from fnmatch import translate


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
            self.transaction_cost = 100

            self.balance-=amount + self.transaction_cost
            

            # self.last_balance= self.balance-self.transaction_cost
            self.withdrawals.append(amount)
            return f"You have withdrawn {amount},transaction cost is {self.transaction_cost} your balance is {self.balance}", self.withdrawals
# Add a new method called deposits_statement which prints each deposit in a new line
    def deposits_statements(self):
        for amount in self.deposits:
            print(f"You have deposited {amount}")
#  Add a new method called withdrawals_statement which prints each withdrawal in a new line
    def withdrawals_statement(self):
    #  print(*self.withdrawals, sep = "\n" )
         for amount in self.withdrawals:
            print(f"You have withdrawn {amount}")

    #  Add a method to show the current balance

    def show_balance(self):
        print(f"You have withdrawn{self.withdrawals}, transaction cost is {self.transaction_cost}, your balance is {self.balance}")
    