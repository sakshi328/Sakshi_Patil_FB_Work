class Student:
    inName="FBS"
    @staticmethod
    def setInName(niname):
        Student.inName=niname


    def __init__(self,frn,name,bname):
        self.frn = frn
        self.name = name
        self.bname = bname
    
        
    def getfrn(self):
        return self.frn
    def setfrn(self,newfrn):
        self.frn = newfrn
            
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name = newname
            
    def getbname(self):
        return self.bname
    def setbname(self,newbname):
        self.bname = newbname
        

  
        
    def display(self):
        print(f"Frn={self.frn}\tName={self.name}\tBname={self.bname}\tIname={Student.inName}")


s1 = Student(12,"Gaurav","17April")
s2 = Student(22,"Pramod","17April")

print(Student.inName)
s1.display()
Student.setInName("Firstbitsolution")
print(Student.inName)
s1.display()