#Write a program to input all sides of a triangle and check whether triangle is valid or not
#Triangle valid hone kai liye
#a+b>c
#a+c>b
#b+c>a

a=int(input("enter a first Side:"))
b=int(input("enter a second side:"))
c=int(input("enter a third side:"))

if(a+b>c and a+c>b and b+c>a):
    print("traingle is valid")
    
else:
    print("traingle is not valid")