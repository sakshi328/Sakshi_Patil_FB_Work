class Bank:
    def __init__(self, id1, name1, balance1):
        self.id = id1
        self.name = name1
        self.balance = balance1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getBalance(self):
        return self.balance

    def setBalance(self, newbalance):
        self.balance = newbalance

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tBalance={self.balance}")


# Bank ends here


class SavingsAccount(Bank):
    def __init__(self, id, name, balance, interest):
        super().__init__(id, name, balance)
        self.interest = interest

    def getInterest(self):
        return self.interest

    def setInterest(self, ninterest):
        self.interest = ninterest
        
    def calBalance(self):
        print(f"Total Balance " )        

    def display(self):
        print(f"Interest={self.interest}")
        super().display()


# SavingsAccount ends here


class CurrentAccount(Bank):
    def __init__(self, id, name, balance, limit):
        super().__init__(id, name, balance)
        self.limit = limit

    def getLimit(self):
        return self.limit

    def setLimit(self, nlimit):
        self.limit = nlimit

    def display(self):
        print(f"Limit={self.limit}")
        super().display()


# CurrentAccount ends here

b1 = Bank(10, "Sachin", 50000)
s1 = SavingsAccount(7, "Harman", 8436, 5)
c1 = CurrentAccount(63, "Surya", 8956, 10000)

b1.display()
s1.display()
c1.display()