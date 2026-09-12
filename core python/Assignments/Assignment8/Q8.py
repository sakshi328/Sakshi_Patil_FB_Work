#8. Write a program find reverse of a number[T-2]
def reverse(num):
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    print("Reverse=",rev)
num=int(input("Enter number:"))
reverse(num)