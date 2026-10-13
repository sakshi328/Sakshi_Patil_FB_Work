#2. Write a program to find factorial of given number using recursion
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
num=int(input("enter a number:"))
print(factorial(num))