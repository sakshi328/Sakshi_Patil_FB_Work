# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book:
    count=0
    def __init__(self,bid=0,bname="Not given", price=0,author="not given"):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        
        Book.count +=1
    def __del__(self):
        print("Book object is destroyed")
        
    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author) 
    
    @staticmethod
    def ShowCount():
        print("Total object created:",Book.count)
        
b1=Book()
b1.ShowBook()
print("---------")

b2=Book(101,"python",450,"ABC")
b2.ShowBook()

b3=Book(102,"Science",750,"SDF")
b3.ShowBook()

print("--------")

Book.ShowCount()