#write a program to check if given 3 digit number is a palindrome or not.
num=int(input("enter a 3 digit number:"))

first=num//100
last=num%10

if first==last:
    print("Palidrome number")
    
else:
    print("Not pallidrome number")