class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def getName(self):
        return self.name

    def setName(self,newname):
        self.name = newname

    def getPrice(self):
        return self.price

    def setPrice(self,newprice):
        self.price = newprice

    def display(self):
        print(f"Name={self.name}\tPrice={self.price}")


p1 = Product("Laptop",50000)

print(p1.getName())
print(p1.getPrice())

p1.display()

p1.setName("Mobile")
p1.setPrice(45000)

p1.display()