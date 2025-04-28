class BankAccount:
    def __init__(self):
        self.__balance = 0 #private
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())    #100
account.withdraw(30)
print(account.get_balance())    #70 = the money left in account
