#3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook
class Shirt:
    def __init__(self,sid=0,sname="Sakshi",type="not define",price=0,size=20):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size
        
    def __del__(self):
        print("shirt object is destroyed")
    
    def showShirt(self):
        print("sid=",self.sid)
        print("sname",self.sname)
        print("stype=",self.type)
        print("price=",self.price)
        print("size=",self.size)
        
s1=Shirt()
s1.showShirt()
print("--------")

s2=Shirt(11,"Sakshi","Formal",23000,21)
        