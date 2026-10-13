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
        
    def display(self):
        print(f"Id={self.id}\tName={self.name}\tsal={self.sal}")
e1=Employee(10,"Sachin", 121212)
e2=Employee(18,"Virat", 33424)
# print(e1.getName())
e1.display()
e2.display()
e2.setSal(8965)
e2.display()