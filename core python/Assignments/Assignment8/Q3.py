# 3. Write a program to find sum of following series using functions : (T-1)
#a. 1 + 2 + 3 + ... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

#1 + 2 + 3 + ... + n
def sum_series():
    n=int(input("Enter number:"))
    sum=0
    
    for i in range(1,n+1):
        sum=sum+i
    print("Sum", sum)
sum_series()

#2.1! + 2! + 3! + 4! + ..... + n!
def factorial_series():
    n=int(input("Enter number:"))
    sum=0
    fact=1
    
    for i in range(1,n+1):
        fact=fact*i
        sum=sum+fact
    print("Factorial series sum=", sum)
factorial_series()

# c. 1^1 + 2^2 + 3^3 + ...... + n^n
def power_series():
    n=int(input("Enter n:"))
    sum=0
    for i in range(1,n+1):
        sum=sum+i**i
    print("Power series sum=", sum)
    
power_series()