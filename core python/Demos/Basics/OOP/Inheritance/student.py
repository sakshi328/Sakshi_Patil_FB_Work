class Student:
    stCount=0
    def __init__(self,frn,name,bname):
        self.frn=frn
        self.name=name
        self.batch=bname  
        Student.stCount+=1
    def display(self):
        print("FRN={self.frn}\tName={self.name}\t Batch={self.batch} \tStudent Count=[Student.stCount]")
       
class PlacedStudent(Student):
    def __init__(self,frn,name,bname,cName):
        super().__init__(frn,name,bname)
        self.cName=cName
    def setCname(self,cName):
        self.cName=cName
    def getCName(self):
        return self.cName
    
    def display(self):
        print(f"CName={self.cName}\t")
        super().display()


s1=Student(12,"Gaurav","April")
s2=Student(1,"Atharav", "Jul/aug")
s3=Student(53,"Rutika", "Jul/aug")
s4=PlacedStudent(37,"Virat", "Jul/aug", "TCS")
s5=PlacedStudent(18,"Virat", "Jul/aug", "one8")
print(Student.stCount)
        
        