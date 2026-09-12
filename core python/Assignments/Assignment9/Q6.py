#6. Write a program to print Fibonacci series using recursion.
def fib(n, a=0, b=1):

    if(n==0):
        return

    print(a, end=" ")

    fib(n-1, b, a+b)


n=int(input("Enter number of terms:"))

fib(n)