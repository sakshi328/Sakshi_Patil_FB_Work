import math
r=20
length=50
breadth=40

#perimeter of semicircle+remaining side of rectangle
perimeter=(math.pi*r)+length+length+breadth

#Fencing 5 times
total_wire=perimeter*5

#cost
cost=total_wire*35

print("Total cost of fencing=", cost)