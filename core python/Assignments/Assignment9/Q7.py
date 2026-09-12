#7. Write a program to find sum of digits using recursion.
def sum_digit(num, sum=0):

    if(num==0):
        return sum

    rem=num%10
    sum=sum+rem
    num=num//10

    return sum_digit(num, sum)


num=int(input("Enter number:"))

print("Sum of digits=", sum_digit(num))