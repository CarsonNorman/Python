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


class User:
    def __init__(self, name, email):
        self.name = name;
        self.email = email;
        self.account = BankAccount(7, 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(self.account.balance)
        return self
    def transfer_money(self,amount,other_user):
        if(isinstance(other_user, User)):
            other_user.account.balance += amount
            self.account.balance -= amount
        else:
            print("No User Found: Transfer Cancelled")
        return self



Harry = User("Harry", "mas@hot.com")
Jacob = User("Jacob", "TurkeyBoy@jacob.com")
Harry.make_deposit(1000).display_user_balance().transfer_money(100, Jacob).display_user_balance()
Jacob.display_user_balance()
