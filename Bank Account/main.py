class BankAccount:
    def __init__(self, int_rate = 7, balance= 1000): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            print (f"Insufficent Funds: Transaction to withdraw {amount}$ Cancelled")
            return self

    def display_account_info(self):
        print(f"Int Rate:{self.int_rate}%, Balance:{self.balance} ")
    
    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance * (self.int_rate/100)
            return self
        else:
            print("Negative Account Balance.  Deposit More Funds")
            return self

peter = BankAccount()
peter.deposit(100).deposit(200).deposit(300).withdraw(1200).yield_interest().display_account_info()

paul = BankAccount()
paul.deposit(1000).deposit(100).withdraw(50).withdraw(25).withdraw(1000).withdraw(1000000).yield_interest().display_account_info()