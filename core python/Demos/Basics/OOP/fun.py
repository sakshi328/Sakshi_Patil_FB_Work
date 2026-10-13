class Employee:
    def init_(self):
        print("I am in con of employee", id(self))
    def display(self):
        print("I am from Display of employee")
        
e1=Employee()
e2=Employee()
print(f"id e1={id(e1)}")
print(f"id e1={id(e2)}")