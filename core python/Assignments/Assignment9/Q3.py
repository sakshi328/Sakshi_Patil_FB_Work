#3. Write a program to reverse a given number using recursive function.
def reverse(num, rev=0):
    if num==0:
        print("Reverse number=", rev)
        return
    
    d=num%10
    rev=rev*10+d
    reverse(num//10,rev)
    
num=int(input("Enter number:"))

reverse(num)