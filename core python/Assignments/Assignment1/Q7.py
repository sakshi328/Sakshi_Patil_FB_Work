#Program to Find the Roots of a Quadratic Equation

a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))

d= b**2-4*a*c

root1=(-b+d**0.5)/(2*a)
root2=(-b-d**0.5)/(2*a)

print("Root 1 =", root1)
print("Root 2=", root2)