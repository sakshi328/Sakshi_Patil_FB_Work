
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

    def display(self):
        print(f"Id={self.id}\tBrand={self.brand}\tPrice={self.price}")


class Car(Vehicle):
    def __init__(self,id,brand,price,seats):
        super().__init__(id,brand,price)
        self.seats=seats
        
    def getSeats(self):
        return self.seats
    def setSeats(self,nseats):
        self.seats=nseats
        
    def display(self):
        print(f"Seats={self.seats}")
        super().display()
        
class Bike(Vehicle):
    def __init__(self,id,brand,price,color):
        super().__init__(id,brand,price)
        self.color=color
        
    def getColor(self):
        return self.color
    def setColor(self,ncolor):
        self.color=ncolor
    
    def display(self):
        print(f"Color={self.color}\t")
        super().display()
        
v1 = Vehicle(1, "Tata", 800000) 
c1 = Car(2, "Honda", 900000, 5) 
b1 = Bike(3, "Honda", 100000, 50)

v1.display()
c1.display()
b1.display()

