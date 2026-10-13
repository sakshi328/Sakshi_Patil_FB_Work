class Instrument:
    def __init__(self, id1, name1, price1):
        self.id = id1
        self.name = name1
        self.price = price1

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


class Guitar(Instrument):
    def __init__(self, id, name, price, strings):
        super().__init__(id, name, price)
        self.strings = strings

    def getStrings(self):
        return self.strings
    def setStrings(self, nstrings):
        self.strings = nstrings
    
    def calPrice(self):
        print(f"Total price of guitar={self.price+self.strings}")

    def display(self):
        print(f"Strings={self.strings}")
        super().display()


class Piano(Instrument):
    def __init__(self, id, name, price, keys):
        super().__init__(id, name, price)
        self.keys = keys

    def getKeys(self):
        return self.keys
    def setKeys(self, nkeys):
        self.keys = nkeys
    
    def calPrice(self):
        print(f"Total price of piano={self.price+self.keys}")
    def display(self):
        print(f"Keys={self.keys}")
        super().display()


i1 = Instrument(1, "Instrument", 5000)
g1 = Guitar(2, "Yamaha Guitar", 15000, 6)
p1 = Piano(3, "Casio Piano", 25000, 61)

i1.display()
g1.display()
p1.display()

