class Student:
    def __init__(self, name, roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
        
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
        
    def getroll(self):
        return self.roll
    def setname(self,newroll):
        self.roll=newroll
        
    def getMarks(self):
        return self.marks
    def setMarks(self,newmarks):
        self.marks = newmarks
        
    def display(self):
        print(f"Name={self.name}\t roll={self.roll}\t Marks={self.marks}")
s1=Student("Rohit", 2, 85)
s1.display()

s1.setMarks(92)
s1.display()
    
    
    
    
    
    
    
    
    
    
    
    
        