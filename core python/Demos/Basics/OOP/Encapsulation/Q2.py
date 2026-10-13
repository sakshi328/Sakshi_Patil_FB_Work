class BankAccount:
    def __init__(self,name,accno,balance):
        self.name=name
        self.accno=accno
        self.balance=balance
    
    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname
        
    def getAccno(self):
        return self.accno
    def setAccno(self,newaccno):
        self.accno=newaccno
        
    def getBalance(self):
        return self.balance
    def setBalance(self,newbalance):
        self.balance=newbalance
        
    def display(self):
        print(f"Name={self.name}\tAccno={self.accno}\tBalance={self.balance}")
        
e1=BankAccount("Rohit", 123456, 50000)
print(e1.getName())

e1.display()

e1.setName("Sakshi")
e1.display()
