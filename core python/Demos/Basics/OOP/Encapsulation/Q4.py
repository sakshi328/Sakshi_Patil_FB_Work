class car:
    def __init__(self, model, brand,price):
        self.model = model
        self.brand = brand
        self.price = price
        
    def getModel(self):
        return self.model
    def setModel(self,newmodel):
        self.model = newmodel
        
    def getBrand(self):
        return self.brand
    def setBrand(self,newbrand):
        self.brand=newbrand
        
    def getPrice(self):
        return self.price
    def setprice(self,newprice):
        self.price=newprice
        
    def display(self):
        print(f"Model={self.model}\tBrand={self.brand}\tPrice={self.price}")
e1=car("Swift","Maruti",800000)
print(e1.getModel())
e1.display()

e1.setprice(750000)
e1.display()
