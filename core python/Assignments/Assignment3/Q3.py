#Write a program to input angles of a triangle and check whether triangle is valid or not.
#a+b+c=180

a=int(input("Enter first angle:"))
b=int(input("Enter second angle:"))
c=int(input("enter third angle:"))
#sum=a=b+c

if(a+b+c==180):
    print("Triangle is valid")
else:
    print("Traingle is not valid.")