
class Animal:
    def __init__(self, id, age, color):
        self.id = id
        self.age = age
        self.color = color

    def getID(self):
        return self.id

    def setID(self, nID):
        self.id = nID

    def getAge(self):
        return self.age

    def setAge(self, nage):
        self.age = nage

    def getColor(self):
        return self.color

    def setColor(self, ncolor):
        self.color = ncolor

    def display(self):
        print(f"Id={self.id}\tAge={self.age}\tColor={self.color}")


class Dog(Animal):
    def __init__(self, id, age, color, breed):
        super().__init__(id, age, color)
        self.breed = breed

    def getBreed(self):
        return self.breed

    def setBreed(self, nbreed):
        self.breed = nbreed

    def display(self):
        print(f"Breed={self.breed}")
        super().display()


class Cat(Animal):
    def __init__(self, id, age, color, food):
        super().__init__(id, age, color)
        self.food = food

    def getFood(self):
        return self.food

    def setFood(self, nfood):
        self.food = nfood

    def display(self):
        print(f"Food={self.food}")
        super().display()


a1 = Animal(10, 2, "Brown")
d1 = Dog(12, 3, "White", "Labrador")
c1 = Cat(13, 3, "Black", "Biscuit")


a1.display()
d1.display()
c1.display()