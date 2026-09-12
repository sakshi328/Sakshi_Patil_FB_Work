#Write a program to check whether the triangle is equilateral, isosceles or scalene traingle
#Equilateral- All three side are equal
#isosceles- Any two side are equal
#Scalene- All three side are different

a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))

if(a==b and b==c):
    print("Equilateral Traingle")
    
elif(a==b or b==c or a==c):
    print("Isosceles Traingle")
    
else:
    print("Scalene Traingle")