# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product:
    def __init__(self,pid=0,pname="Not given",price=0,quantity="Not given"):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
        
    def __del__(self):
        print("Product object is destroyed")
        
    def showProduct(self):
        print("pid=",self.pid)
        print("pname",self.pname)
        print("price=",self.price)
        print("quantity=",self.quantity)
        
p1=Product()
p1.showProduct()
print("-----------")
p2=Product(101,"Laptop",45000,2)
p2.showProduct()

