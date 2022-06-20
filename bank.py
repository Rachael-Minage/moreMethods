from time import strftime


class Account:
    def __init__(self,account_name,account_number):
        # self.withdraw = withdraw
        self.account_name = account_name
        self.account_number =account_number
        # self.deposit = deposit 
        self.balance = 0
        self.deposit_list = []
        self.withdrawals_list = []
        self.datetime =strftime("%d-%-m-%Y %-I:%M%P")
        self.loan_balance = 0
        self.interest = 0.03
        


        
    def deposits(self,amount):
        if amount<=0:
            return f"Cannot deposit a negative amount or zero"
        else:

          self.balance+=amount
          self.deposit_list.append({"date":self.datetime,"amount":amount,"narration":"deposit"})
          return f"You have deposited {amount}. Your balance is {self.balance}", self.deposit_list

    def withdrawal(self,amount):
       self.transaction_cost = 100
 
       if (amount+ self.transaction_cost)  > self.balance:
           return f"Your balance is {self.balance}, you cannot withdraw {amount}"
       elif (amount + self.transaction_cost)<=0:
           return f"You cannot withdraw {amount}"
       else:
          
 
           self.balance-=(amount + self.transaction_cost)
          
 
           # self.last_balance= self.balance-self.transaction_cost
           self.withdrawals_list.append({"date":self.datetime,"amount":amount,"narration":"withdrawal"})
           return f"You have withdrawn {amount},transaction cost is {self.transaction_cost} your balance is {self.balance}", self.withdrawals_list
# Add a new method called deposits_statement which prints each deposit in a new line
    def deposits_statements(self):
       for x in self.deposit_list:
           print(x)
#  Add a new method called withdrawals_statement which prints each withdrawal in a new line
    def withdrawals_statement(self):
   #  print(*self.withdrawals, sep = "\n" )
        for x in self.withdrawals_list:
           print(x)
 
   #  Add a method to show the current balance
 
    def show_balance(self):
       print(f"Your balance is {self.balance}")
   
    
    def full_statement(self):
        statement_list = self.deposit_list + self.withdrawals_list
        for i in statement_list:
            print (i)

    def borrow(self,amount):
        sum_of_deposits = 0
        for i in self.deposit_list:
            sum_of_deposits+=i["amount"]
        if len(self.deposit_list)<10:
            return "Loan denied you have deposited less than 10 times in this account"
        elif amount<100:
            return f"Loan denied amount requested must be more than 100. You have borrowed{amount}"
        elif amount>=(sum_of_deposits//3) :
            return f"Loan denied.{amount} is greater that 1/3 of total deposits"
        elif self.balance==0:
            return f"Your balance is{self.balance}. You do not qualify for a loan"
        elif self.loan_balance >0:
            f"Loan denied. You have an outstanding loan of {self.loan_balance}"

        else:

            self.loan_balance+=amount
            total_loan = self.loan_balance+ (self.interest*amount)
            self.balance += self.loan_balance
            return f"Loan accepted. Your loan is {self.loan_balance}.Loan plus interest is {total_loan}.Your account balance is {self.balance}"
    def loan_repayment(self,amount):
        if amount< self.loan_balance:
            self.loan_balance-=amount
            return f"You have repaid {amount}. Outstanding balance is {self.loan_balance}"
        elif amount == self.loan_balance:
            self.loan_balance-=amount
            return f"You have repaid {amount}. Your loan is fully paid."
        elif amount > self.loan_balance:
            overpayment = amount - self.loan_balance
            remaining_balance = amount-overpayment
            self.balance+=overpayment
            self.loan_balance-=remaining_balance
            return f"You have repaid {amount}, Your loan balance is {self.loan_balance}. Your account balance is {self.balance}"

    def transfer(self,amount,account_instance):
        if amount > self.balance:
            return f"You have insufficient balance to transfer {amount}"
        elif amount <=0:
            return f"{amount} is invalid"
        else:
            self.balance-=amount
            account_instance.balance += amount
            return f"You have transfered {amount} to {account_instance.account_name}. Your balance is {self.balance}"




            


            





