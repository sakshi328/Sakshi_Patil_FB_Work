# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.


class Product:
    discount = 10

    def __init__(self, pid=21, pname="Sakshi", price=765, quantity=2):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print("Product object is destroyed")

    def showProduct(self):
        print("pid =", self.pid)
        print("pname =", self.pname)
        print("price =", self.price)
        print("quantity =", self.quantity)

    @staticmethod
    def applyDiscount(price):
        dis = price * Product.discount / 100
        finalPrice = price - dis
        print("Final price after discount is:", finalPrice)


p1 = Product()
p1.showProduct()

print("-----------")

p2 = Product(101, "Laptop", 45000, 2)
p2.showProduct()
Product.applyDiscount(p2.price)
