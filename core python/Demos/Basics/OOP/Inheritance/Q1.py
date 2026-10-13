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

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tPrice={self.price}")

class Laptop(Electronics):
    def __init__(self, id, name, price, ram):
        super().__init__(id, name, price)
        self.ram = ram

    def getRam(self):
        return self.ram
    def setRam(self, nram):
        self.ram = nram

    def display(self):
        print(f"RAM={self.ram}")
        super().display()

class Mobile(Electronics):
    def __init__(self, id, name, price, camera):
        super().__init__(id, name, price)
        self.camera = camera

    def getCamera(self):
        return self.camera
    def setCamera(self, ncamera):
        self.camera = ncamera

    def display(self):
        print(f"Camera={self.camera}")
        super().display()


e1 = Electronics(1, "TV", 40000)
l1 = Laptop(2, "HP", 55000, "8GB")
m1 = Mobile(3, "Samsung", 25000, "50MP")

e1.display()
l1.display()
m1.display()

