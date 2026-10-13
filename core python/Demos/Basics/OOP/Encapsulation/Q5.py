class Teacher:
    def __init__(self,tid,name,subject,salary):
        self.tid = tid
        self.name = name
        self.subject = subject
        self.salary = salary

    def gettid(self):
        return self.tid

    def settid(self,newtid):
        self.tid = newtid

    def getname(self):
        return self.name

    def setname(self,newname):
        self.name = newname

    def getsubject(self):
        return self.subject

    def setsubject(self,newsubject):
        self.subject = newsubject

    def getsalary(self):
        return self.salary

    def setsalary(self,newsalary):
        self.salary = newsalary

    def display(self):
        print(f"Id={self.tid}\tName={self.name}\tSubject={self.subject}\tSalary={self.salary}")


t1 = Teacher(1,"Rahul","Python",50000)
t2 = Teacher(2,"Sneha","Java",60000)

t1.display()
t2.display()