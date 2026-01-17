class account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self._balance = balance

    def deposit(self, a):
        if a > 0:
            self._balance += a

    def withdraw(self, a):
        if a > 0 and a < self.__balance:
            self.__balance -= a
            
    def getbalance(self):
        return self._balance

    def getaccountnum(self):
        return self.__account_number



class SavingsAccount(account):
    def description(self):
        return type(self)
        
    def __init__(self, account, number, interest):
        super().__init__(account_number, balance)
        if interest == None:
            self.interest = 0.02
        else:
            self.interest = interest

    def annual_interest(self):
        return self._balance*self.interest


class CurrentAccount(account):
    def __init__(self, account_number, balance, overdraft):
        super().__init__(account_number, balance)
        if overdraft == None:
            self.overdraft = 100
        else:
            self.overdraft = overdraft

    def withdraw(self, c):
        if (c > 0) and (c < self._balance + self.overdraft):
            self._balance -= c            


pweez = CurrentAccount(3, 70, 900)
print(pweez.getbalance())
pweez.withdraw(500)
print(pweez.getbalance())
