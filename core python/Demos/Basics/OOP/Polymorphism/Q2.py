class Vehicle:
    def __init__(self, id, brand, price):
        self.id = id
        self.brand = brand
        self.price = price

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getBrand(self):
        return self.brand

    def setBrand(self, newbrand):
        self.brand = newbrand

    def getPrice(self):
        return self.price

    def setPrice(self, newprice):
        self.price = newprice
    
    def calPrice(self):
        print(f"Total price{self.price}")

    def display(self):
        print(f"Id={self.id}\tBrand={self.brand}\tPrice={self.price}")


class Car(Vehicle):
    def __init__(self,id,brand,price,insurance):
        super().__init__(id,brand,price)
        self.insurance=insurance
        
    def getInsurance(self):
        return self.seats
    def setInsurance(self,ninsurance):
        self.seats=ninsurance
    
    def calPrice(self):
        print(f"Final price of car={self.price+self.insurance}")
    def display(self):
        print(f"Insurance={self.insurance}")
        super().display()
        
class Bike(Vehicle):
    def __init__(self,id,brand,price,accessories):
        super().__init__(id,brand,price)
        self.Accessories=accessories
        
    def getAccessories(self):
        return self.accessories
    def setAccessories(self,naccessories):
        self.Accessories=naccessories
    
    def calAccessories(self):
        print(f"total price of bike:{self.price+self.accessories}")
    def display(self):
        print(f"Color={self.color}\t")
        super().display()
        
v1 = Vehicle(1, "Tata", 800000) 
c1 = Car(2, "Honda", 900000, 5) 
b1 = Bike(3, "Honda", 100000, 50)

v1.calPrice()
c1.calPrice()
b1.calPrice()

