class Employee:
    def __init__(self,id1,name1,sal1):
        self.id=id1
        self.name=name1
        self.sal=sal1
        
    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid       
        
    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname       
        
    def getSal(self):
        return self.sal
    def setSal(self,newsal):
        self.sal=newsal
        
    def __str__(self):
        return f"Id={self.id}\tName={self.name}\tsal={self.sal}"
        
#EMP ends here

class Hr(Employee):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com=com
    def getCom(self):
        return self.com
    def setCom(self,ncom):
        self.com=ncom

    def __str__(self):
        return super().__str__() + f"\tCom={self.com}"
  
#Class HR ends here-----
class Developer(Employee):
    def __init__(self,id,name,sal,bonus):
        super().__init__(id,name,sal)
        self.bonus=bonus
    def getBonus(self):
        return self.bonus
    def setBonus(self,nbonus):
        self.bonus=nbonus

    def str__(self):
        return super().__str__() + f"\tBonus={self.bonus}"
       

        
e1=Employee(10,"Sachin", 121212)
h1=Hr(7,"Harman",8436,1500)
d1=Developer(63,"Surya",8956,563)

print(e1)
print(h1)
print(d1)