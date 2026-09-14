import math
length=float(input("Enter length:"))
breadth=float(input("Enter breadth:"))
radius=float(input("Enter radius"))

area_rectangle=length*breadth
area_semicircle=(math.pi*radius*radius)/2

total_area=area_rectangle+area_semicircle

perimeter=length+length+breadth+(math.pi*radius)
print("area=",total_area)
print("perimeter=", perimeter)