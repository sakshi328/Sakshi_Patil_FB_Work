# 7. Write a program to find sum of digits of a number.
def sum_of_digits():
    num=int(input("Enter number:"))
    sum=0
    
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
        
    print("Sum of digits=", sum)
sum_of_digits()
        