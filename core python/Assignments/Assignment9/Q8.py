#8. Write a program to check whether a number is prime or not using recursion.
def prime(num, i=1, count=0):

    if(i > num):
        if(count == 2):
            return "Prime number"
        else:
            return "Not Prime Number"

    if(num % i == 0):
        count += 1

    return prime(num, i+1, count)


num=int(input("Enter number:"))

result=prime(num)

print(result)