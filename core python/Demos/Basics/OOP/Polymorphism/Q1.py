class Electronics:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def getId(self):
        return self.id
    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getPrice(self):
        return self.price
    def setPrice(self, newprice):
        self.price = newprice
    
    def calPrice(self):
        print(f"Total price{self.price}")
        
    def display(self):
        print(f"Id={self.id}\tName={self.name}\tPrice={self.price}")
#Electronics ends here  

class Laptop(Electronics):
    def __init__(self, id, name, price, warranty):
        super().__init__(id, name, price)
        self.warranty = warranty

    def getWarranty(self):
        return self.warranty
    def setWarranty(self, nwarranty):
        self.warranty = nwarranty
    
    def calPrice(self):
        print(f"Total price of laptop={self.price + self.warranty}")

    def display(self):
        print(f"Warranty={self.warranty}")
        super().display()

class Mobile(Electronics):
    def __init__(self, id, name, price, charger):
        super().__init__(id, name, price)
        self.charger = charger

    def getCharger(self):
        return self.charger
    def setCharger(self, ncharger):
        self.charger = ncharger

    def calPrice(self):
        return super().calprice()
    
    def calPrice(self):
        print(f"Total price of mobile={self.price+self.charger}")
        
    def display(self):
        print(f"Charger={self.charger}")
        super().display()


e1 = Electronics(1, "TV", 40000)
l1 = Laptop(2, "HP", 55000, 70000)
m1 = Mobile(3, "Samsung", 25000, 34000)

e1.calPrice()
l1.calPrice()
m1.calPrice()
