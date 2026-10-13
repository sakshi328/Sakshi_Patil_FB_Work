
class Animal:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def calFood(self):
        print("Animal food cost")

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tAge={self.age}")


class WildAnimal(Animal):
    def __init__(self, id, name, age, meat):
        super().__init__(id, name, age)
        self.meat = meat

    def calFood(self):
        print(f"Food cost of wild animal={self.meat * 2}")

    def display(self):
        print(f"Meat={self.meat}")
        super().display()


class DomesticAnimal(Animal):
    def __init__(self, id, name, age, grains):
        super().__init__(id, name, age)
        self.grains = grains

    def calFood(self):
        print(f"Food cost of domestic animal={self.grains + 500}")

    def display(self):
        print(f"Grains={self.grains}")
        super().display()


a1 = Animal(1, "Animal", 5)
w1 = WildAnimal(2, "Lion", 8, 5000)
d1 = DomesticAnimal(3, "Cow", 4, 1000)

a1.calFood()
w1.calFood()
d1.calFood()

